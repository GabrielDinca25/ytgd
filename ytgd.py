import youtube_dlc
import threading
import sys
import getopt


def download_single_video(ydl, url):
    ydl.download([url])

args = sys.argv[1:]

if len(args) != 2:
    print("Incorrect argument number (should be 2). E.g. ytgd.py <playlist-url> <file-format>")
    sys.exit(0)

playlist_url = args[0]
file_format = args[1]

ydl_opts = {
    'writesubtitles': True,
    'format': file_format,
    'writethumbnail': True
}

video_urls = []

with youtube_dlc.YoutubeDL(ydl_opts) as ydl:
    ie_result = ydl.extract_info(playlist_url, False)
    
    #print(ie_result)

    if 'entries' in ie_result:
        videos = ie_result['entries']

        for i, item in enumerate(videos):
            video_urls.append(videos[i]['webpage_url'])

        print(video_urls)

    #for url in video_urls:
        #ydl.download([url])

    threads = []
    for url in video_urls:
        t = threading.Thread(target=download_single_video, args=(ydl, url))
        threads.append(t)

    for t in threads:
        t.start()