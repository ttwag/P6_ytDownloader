import subprocess
import getpass
from pytube import YouTube
from pytube import helpers
from moviepy.editor import *
from sys import argv
"""
This python program 

"""
# Get the video and specify its filename
if len(argv) == 1:  # Check Input
    print("Give Me A YouTube Link")
    exit()
link = argv[1]
yt = YouTube(link)
name = yt.title
if len(argv) == 3:
    name = argv[2]

title = helpers.safe_filename(name)  # Need to comply the pytube library video naming standards
print("Title: ", yt.title)
print("File Name: ", name)
print("Author: ", yt.author)  # Change this to something else
yt.streams.get_highest_resolution().download(filename=title+".mp4")

# Create file path for mp4 to mp3
input_mp4 = "./" + title + ".mp4"
user = getpass.getuser()  # Get the username for file path
output_mp3 = "/Users/" + user + "/Music/Music/Media.localized/Music/Unknown Artist/Unknown Album/" + title + ".mp3"
video = VideoFileClip(input_mp4)

# mp4 to mp3 conversion - Extract audio and save as MP3
audio = video.audio
audio.write_audiofile(output_mp3, codec='libmp3lame', bitrate='130k')

# Close video file
video.close()

# Delete the .mp4 file
delete_mp4 = "rm " + "./" + '"' + title + '"' + ".mp4"
subprocess.run(delete_mp4, shell=True)

# Open the .mp3 file
open_mp3 = "open " + '/Users/' + user + '/Music/Music/Media.localized/Music/"Unknown Artist"/"Unknown Album"/' + '"' + title + ".mp3" + '"'
subprocess.run(open_mp3, shell=True)

# Download Successful
print("Download Successful!!")
