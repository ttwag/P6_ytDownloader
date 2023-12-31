# P6_ytDownloader
Help macOS users download YouTube music through the command line interface. The music is downloaded to
the appropriate music folder used by the Music app on macOS.

![Figure1](./media/Figure1.png)

**Video Demonstration**



https://github.com/ttwag/P6_ytDownloader/assets/113254272/aef7cfc8-c61d-44b5-b47c-a0fe93ce1bd6



You can watch the demo.mp4 in the media folder of the repository for how to use this tool.

## Installation
This program only runs with **macOS**.

### Method 1
Open **Terminal** in Mac and enter these **2 commands** in your home directory for installation:

```$ git clone "https://github.com/ttwag/P6_ytDownloader/tree/main"```

```$ mv $HOME/P6_ytDownloader/yt.sh $HOME/```

### Method 2
Download the .zip file from This GitHub Page -> Code -> Download ZIP and unzip the file.

Open **Terminal** and move the unzipped folder from download to your home directory by

```$ mv $HOME/Downloads/P6_ytDownloader-main $HOME/P6_ytDownloader```

then 

```$ mv $HOME/P6_ytDownloader/yt.sh $HOME/```

### Note for Method 1:

Your computer needs **git** to be installed, which may require you to install the **homebrew** package installer.

If you haven't installed git, do ```$ brew install git```. 
If the brew command is not found, do 

```$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```

to install homebrew or visit https://brew.sh for more help.

## How to Use This Program
### Download YouTube Music
In the home directory where you downloaded this program, do 

```$ zsh yt.sh "video's url" "file name of your choice"[optional]```

yt.sh is a shell script that starts the program. 

You also need to give the video's URL and the optional file name. If no file name is given, 
the default video title from YouTube is used. Remember to surround the inputs with quotation marks.

## Dependencies and File Structure
* This program is intended to be installed and called in the user's home directory. To go to your home directory, do ```$ cd $HOME```.
* bin and lib contain the files for setting up a Python virtual environment.
* ytDownloader.py contains the main program that downloads YouTube Music, stores it in the desired location, and plays the music.
* The downloaded music is stored in the macOS Music app's library file path ```/Users/username/Music/Music/Media.localized/Music/"Unknown Artist"/"Unknown Album"```

## Development Environment
The Python code was developed using PycharmCE 2023.1.3, and the shell scripts were written via Vim in the macOS terminal.

## Encountered Issues
* There's an issue with the [.get_audio_only](https://github.com/pytube/pytube/issues/203) method in pytube, so this program needs to download
the mp4 video file first and convert it to mp3 file, then delete the mp4. I used moviepy for the conversion.
* Using the Music app in macOS to play .mp3 files also has some caveats. You need to ensure that the .mp3 file is 
encoded with an encoder and bit rate recognizable by the Music app, otherwise, the duration of music could be incorrect. 
Go to Music's settings to see what's recognizable.
* The Python library used by this program, pytube, downloads the music with YouTube video's title as the filename.
However, it removes some special characters through the function safe_filename() in helper.py from pytube's source code.

## Helpful Links
For more information about how to use Python to download music from YouTube, visit https://youtu.be/vEQ8CXFWLZU?si=01VEvh60EG3NU7vM.
I built this program based on Project 2 in the video.
