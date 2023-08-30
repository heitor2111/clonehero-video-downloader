import os
import platform
import sys
import traceback

from alive_progress import alive_bar, alive_it

# Get the source folder
if platform.system() == 'Windows':
    sourceFolder = os.path.expanduser('~') + r'\Documents\Clone Hero'
    os.system('cls')
elif platform.system() == 'Linux':
    sourceFolder = os.path.basename('~') + r'\.clonehero'
    os.system('clear')
elif platform.system() == 'Darwin':
    sourceFolder = os.path.basename('~') + r'\Clone Hero'
    os.system('clear')
else:
    sourceFolder = ''

replaceDownloaded = False
args = sys.argv
args.pop(0)

for arg in args:
    if arg.startswith('--src'):
        sourceFolder = arg.replace('--src=', '')

    if arg.startswith('--replace'):
        replaceDownloaded = True

    if arg.startswith('--help'):
        print('Usage: python main.py [options]')
        print('')
        print('Options:')
        print('  --src=<path>       Path to the Clone Hero folder.')
        print('  --replace          Replace downloaded songs.')
        print('  --help             Show this help message.')
        sys.exit(1)

# If not exists Songs or PlayerData/Songs folder, exit the program with message
if not os.path.isdir(sourceFolder + r'\Songs'):
    if not os.path.isdir(sourceFolder + r'\PlayerData\Songs'):
        print('Não foi possível encontrar a pasta Songs ou PlayerData/Songs dentro da pasta do jogo selecionada:')
        print(sourceFolder)
        sys.exit(1)
    else:
        sourceFolder += r'\PlayerData\Songs'
else:
    sourceFolder += r'\Songs'


# Create a object of the class Songs
class Songs:
    def __init__(self, name, path, video, song_length):
        self.name = name
        self.path = path
        self.video = video
        self.song_length = song_length


# Create a empty list to store the objects of the class Songs
songs = []

# Count the total number of files
folders = os.walk(sourceFolder)
total_files = sum(len(files) for _, _, files in folders)

# Search for song.ini and video.mp4 files recursively inside the sourceFolder
with alive_bar(total_files, bar="smooth", title="Verificando arquivos...") as bar:
    for root, dirs, files in os.walk(sourceFolder):
        for file in files:
            song = Songs('', root, False, 0)

            if file == 'song.ini':
                # Open the song.ini file supporting UTF-8 and read the content
                with open(os.path.join(root, file), 'rt', encoding='utf-8', errors='ignore') as f:
                    content = f.readlines()

                    for line in content:
                        if line.startswith('artist'):
                            artist = line.split('=')[1].strip()
                        elif line.startswith('name'):
                            name = line.split('=')[1].strip()
                        elif line.startswith('song_length'):
                            song.song_length = int(line.split('=')[1].strip()) / 1000

                        if 'artist' in locals() and 'name' in locals():
                            song.name = artist + ' - ' + name

                    # Close file
                    f.close()

                # Check if video.mp4 exists in root folder
                if os.path.isfile(os.path.join(root, 'video.mp4')):
                    song.video = True

                # Create an object of the class Songs and append it to the list
                songs.append(song)

            # Update the progress bar
            bar()

# If replaceDownloaded is False, filter the list to show only songs without video
if not replaceDownloaded:
    songs = list(filter(lambda x: x.video is False, songs))

# Print a count of songs selected
print(f'{len(songs)} songs found.')

# Search for video in YouTube and try to download it
songs = alive_it(songs, bar="smooth", title="Downloading videos...", dual_line=True)
for song in songs:
    songs.text = f'-> {song.name}'

    # Import the YouTube module
    from pytube import Search

    try:
        # Search for the video in YouTube
        search = Search(f"{song.name} Official Video")

        yt = None

        if len(search.results) > 0:
            for result in search.results:
                if song.song_length + 15 >= result.length >= song.song_length - 5:
                    yt = result
                    break

        if yt:
            # Get the video in the best resolution and extract only image
            for stream in yt.streams.filter(only_video=True, file_extension='mp4').order_by('resolution').desc():
                # Check if the video resolution is 1080p or less
                if int(stream.resolution.replace('p', '')) <= 1080:
                    stream.download(song.path, "video.mp4")

                    # Print a message
                    print(f'{song.name}: Downloaded successfully.')

                    break
        else:
            print(f'{song.name}: Video not found.')
    except:
        print('An error occurred while downloading the video.')

# Print a empty line to space the progress bar from the list
print('\n')
