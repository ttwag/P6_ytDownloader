# P6_ytDownloader
Help macOS user to download YouTube music through the command line interface.
Video
## Installation and Usage

## Dependencies and File Structure
* setup
* bin and lib contains the files for setting up a Python virtual environment.
* ytDownloader.py contains the main program that downloads the YouTube Music, storing it to desired location, and play the music.
## Development Environment
The python code was developed using PycharmCE 2023.1.3, and the shell scripts were written via vim in macOS terminal.
## Helpful Links


**What does this program do?**
* When the user enters ```$ zsh yt.sh "url"``` in macOS terminal, the program downloads the .mp3 file of the
music from url. The music will be stored in the Apple Music Library.
* The program automatically plays the music through the Music app, then it deletes 
the downloaded mp4 and mp3 files because the mp3 file would be copied to Music already. 
* The remaining mp3 file will be stored in  
`/Users/taowang/Music/Music/Media.localized/Music/Unknown Artist/Unknown Album/`
* User could optionally add desired filename for the music.

**Dependencies**
* There's an issue with the .get_audio_only method in pytube, so this program needs to download
the mp4 video file first then convert it to mp3 file.
* However, this introduces dependencies on the ffmpeg command line tool, which converts mp4 to mp3.
The user needs to install ffmpeg through ```$ brew intall ffmpeg```, and possibly install Homebrew.
* Or we could do it through Moviepy to convert mp4 to mp3.

**Note**
* Apple Music reads VBR and video with hhigh kbps, so set bit rate to approximate VBR. Import settings in Music
* Needs to run this through its own python interpreter.
* Make sure the file path is right across machines.
* Beaware that when pytube downloads a video the file name may not always be the title. In the source code, the library
uses the function safe_filename() in helper.py from pytube.