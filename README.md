![status: deprecated](https://img.shields.io/badge/status-deprecated-red)

⚠️ **Este projeto está obsoleto e não receberá nenhum suporte ou atualização!** ⚠️  
Recomendamos usar [Geomitron/Bridge](https://github.com/Geomitron/Bridge) em vez deste.




<p style="color:red">This project will no longer receive updates and may not work. It will be rebuilt from scratch with an interface, stay tuned!</p>

# Clone Hero Song Video Downloader

## Summary

- [English](#english)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [Disclaimer](#disclaimer)
- [Português](#português)
  - [Pré-requisitos](#pré-requisitos)
  - [Uso](#uso)
  - [Aviso Legal](#aviso-legal)

## English

This Python script is designed to help you download videos for Clone Hero songs. Clone Hero is a rhythm game that allows you to play custom songs, and sometimes these songs come without videos. This script aims to automate the process of finding and downloading videos for these songs from YouTube.

### Prerequisites

Before using this script, make sure you have the following installed:

- Python
- [pytube](https://python-pytube.readthedocs.io/en/latest/)

You can install `pytube` using pip:

```bash
pip install pytube
```

### Usage

To use this script, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where the script is located.

3. Run the script with Python, and you can use the following options:

   - `--src=<path>`: Specify the path to your Clone Hero folder.
   - `--replace`: Replace downloaded songs.
   - `--help`: Display the help message.

   Example usage:

   ```bash
   python main.py --src=/path/to/clonehero --replace
   ```

   This command will search for songs in the specified Clone Hero folder and attempt to download videos for them.

### Disclaimer

Downloading videos from YouTube may be subject to legal restrictions in your country. Make sure you have the necessary permissions and comply with YouTube's terms of service and copyright policies when using this script.

Use this script responsibly and only for personal use or when you have the right to download and use the videos.

## Português

Este script em Python foi projetado para ajudar a baixar vídeos para as músicas do Clone Hero. O Clone Hero é um jogo de ritmo que permite tocar músicas personalizadas e, às vezes, essas músicas não vêm com vídeos. Este script tem como objetivo automatizar o processo de encontrar e baixar vídeos para essas músicas no YouTube.

### Pré-requisitos

Antes de usar este script, certifique-se de que você tem o seguinte instalado:

- Python
- [pytube](https://python-pytube.readthedocs.io/en/latest/)

Você pode instalar o `pytube` usando pip:

```bash
pip install pytube
```

### Uso

Para usar este script, siga estas etapas:

1. Abra o terminal ou prompt de comando.

2. Navegue até o diretório onde o script está localizado.

3. Execute o script com o Python e você pode usar as seguintes opções:

   - `--src=<path>`: Especifique o caminho para a pasta do Clone Hero.
   - `--replace`: Substituir músicas baixadas.
   - `--help`: Mostrar a mensagem de ajuda.

   Exemplo de uso:

   ```bash
   python main.py --src=/caminho/para/clonehero --replace
   ```

   Este comando procurará músicas na pasta especificada do Clone Hero e tentará baixar vídeos para elas.

### Aviso Legal

Baixar vídeos do YouTube pode estar sujeito a restrições legais em seu país. Certifique-se de ter as permissões necessárias e cumpra os termos de serviço e políticas de direitos autorais do YouTube ao usar este script.

Use este script de forma responsável e apenas para uso pessoal ou quando tiver o direito de baixar e usar os vídeos.
