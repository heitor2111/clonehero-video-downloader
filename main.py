import sys
import platform
import os

# Get the source folder
if platform.system() == 'Windows':
    sourceFolder = os.path.expanduser('~') + r'\Documents\Clone Hero'
elif platform.system() == 'Linux':
    sourceFolder = os.path.basename('~') + r'\.clonehero'
elif platform.system() == 'Darwin':
    sourceFolder = os.path.basename('~') + r'\Clone Hero'
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
        sys.exit(0)

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
    def __init__(self, name, path, video):
        self.name = name
        self.path = path
        self.video = video


# Create a empty list to store the objects of the class Songs
songs = []

# Search for song.ini and video.mp4 files recursively inside the sourceFolder
for root, dirs, files in os.walk(sourceFolder):
    for file in files:
        song = Songs('', root, False)

        if file == 'song.ini':
            # Open the song.ini file supporting UTF-8 and read the content
            with open(os.path.join(root, file), 'rt', encoding='utf-8', errors='ignore') as f:
                content = f.readlines()

                for line in content:
                    if line.startswith('artist'):
                        artist = line.split('=')[1].strip()
                    elif line.startswith('name'):
                        name = line.split('=')[1].strip()

                    if 'artist' in locals() and 'name' in locals():
                        song.name = artist + ' - ' + name

                # Close file
                f.close()

            # Check if video.mp4 exists in root folder
            if os.path.isfile(os.path.join(root, 'video.mp4')):
                song.video = True

            # Create a object of the class Songs and append to the list
            songs.append(song)

# If replaceDownloaded is False, filter the list to show only songs without video
if not replaceDownloaded:
    songs = list(filter(lambda x: x.video is False, songs))

# Search for video in YouTube and try to download it
for song in songs:
    print('Downloading video for song: ' + song.name)

    # Import the YouTube module
    from pytube import Search

    try:
        # Search for the video in YouTube
        search = Search(f"{song.name} Official Music Video")

        if len(search.results) > 0:
            yt = search.results[0]
        else:
            yt = ''

        # Get the video in the best resolution and extract only image
        for stream in yt.streams.filter(only_video=True, file_extension='mp4').order_by('resolution').desc():
            # Check if the video resolution is 1080p or less
            if stream.resolution is not None and int(stream.resolution.replace('p', '')) <= 1080:
                # Download the video
                stream.download(song.path, "video.mp4")
                break

        # Print a message
        print('Video downloaded successfully.')
    except:
        print('Video not found.')
