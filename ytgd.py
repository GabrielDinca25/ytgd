import youtube_dlc
import youtube_dl
import threading
import multiprocessing
import sys
import getopt
import os
import shutil

from custom_youtube_downloader import CustomYouTubeDownloader

args = sys.argv[1:]


ydl_opts = {
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'writesubtitles': False,
    'format': "bestaudio/best",
    'writethumbnail': False,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

video_urls = []

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #ydl.utils.std_headers['Cookie'] = "http://youtube.com/"
    ycd = CustomYouTubeDownloader(ydl)

    ycd.download_playlist("https://youtube.com/playlist?list=PLRfY4Rc-GWzhdCvSPR7aTV0PJjjiSAGMs")
