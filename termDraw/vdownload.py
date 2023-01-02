#!/bin/python3
from pytube import YouTube

link = input("Enter the YouTube video URL: ")

youtubeObject = YouTube(link)
youtubeObject = youtubeObject.streams.get_highest_resolution()
try:
    youtubeObject.download()
except:
    print("An error has occurred")
    raise
print("Download is completed successfully")

# ffmpeg -i 'video' -vf fps=24 ./frame%d.png
