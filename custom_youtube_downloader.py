import youtube_dlc
import threading
import multiprocessing
import sys
import getopt
import datetime

class CustomYouTubeDownloader:
    
    def __init__(self, youtube_downloader):
        self.youtube_downloader = youtube_downloader

    def download_single_video(self, url):
        print(f"Downloading the following video: {url}")
        self.youtube_downloader.download([url])

    def download_videos(self, urls):
        for url in urls:
            self.download_single_video(url)


    def extract_video_urls(self, url):
        video_urls = []

        ie_result = self.youtube_downloader.extract_info(url, False)
    
        #print(ie_result)

        if 'entries' in ie_result:
            videos = ie_result['entries']

            for i, item in enumerate(videos):
                video_urls.append(videos[i]['webpage_url'])

            return video_urls
        else:
            print("Playlist is empty or the URL entered is invalid")

            return []

    def download_playlist(self, playlist_url):
        threads = []

        videos_urls = self.extract_video_urls(playlist_url)

        if videos_urls:
            urls_per_thread_count = 0
            unassigned_urls_count = 0
            urls_count = len(videos_urls)
            cpu_count = multiprocessing.cpu_count()

            if urls_count > cpu_count:
                unassigned_urls_count = urls_count % cpu_count
                urls_per_thread_count = int(urls_count / cpu_count)

                print(f"CPU Cont: {cpu_count}")
                print(f"Unassigned URLS: {unassigned_urls_count}")
                print(f"URL THREAD COUNT: {urls_per_thread_count}")

                buffer = 0
                extra_unassigned_video = 0

                if unassigned_urls_count > 0:
                    extra_unassigned_video = 1

                for i in range(cpu_count):
                    print(f"Thread {i} downloading videos from {buffer} to {buffer + urls_per_thread_count + extra_unassigned_video }")
                    args_sublist = videos_urls[buffer:buffer + urls_per_thread_count + extra_unassigned_video]
                    t = threading.Thread(target=self.download_videos, args=([args_sublist]))
                    buffer = buffer + urls_per_thread_count + extra_unassigned_video

                    if unassigned_urls_count > 0:
                        unassigned_urls_count -= 1

                    if unassigned_urls_count == 0:
                        extra_unassigned_video = 0

                    threads.append(t)
            else:
                for url in videos_urls:
                    print("Found video with URL: ")
                    print(url)
                    print("\n")
                    t = threading.Thread(target=self.download_single_video, args=([url]))
                    threads.append(t)
        else:
            print("No videos to download")

        if threads:
            for t in threads:
                t.start()




