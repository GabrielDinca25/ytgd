import youtube_dlc
import threading
import multiprocessing
import sys
import getopt
import os
import shutil

from custom_youtube_downloader import CustomYouTubeDownloader

args = sys.argv[1:]

# if len(args) != 2:
#     print("Incorrect argument number (should be 2). E.g. ytgd.py <playlist-url> <file-format>")
#     sys.exit(0)

# playlist_url = args[0]
# file_format = args[1]

ydl_opts = {
    #'output': 'E:/repos/Pyhton/YoutubePlaylistDownloader/ytgd/downloads/',
    'writesubtitles': False,
    'format': "bestaudio/best",
    'writethumbnail': False
}

video_urls = []

with youtube_dlc.YoutubeDL(ydl_opts) as ydl:

    ycd = CustomYouTubeDownloader(ydl)

    ycd.download_playlist("https://youtube.com/playlist?list=PLNdHpW28eYAUhHsGPsROtv9DtHIJYBIZr")
