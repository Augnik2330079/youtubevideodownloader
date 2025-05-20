import yt_dlp
import os

def download_youtube_video(url, path):
    # Output template: Save as "Title.mp4" in the chosen directory
    ydl_opts = {
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'format': 'best[ext=mp4]/best',  # Download best mp4 or best available
        'noplaylist': True,  # Only download single video, not playlist
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ").strip()
    path = input("Enter the directory to save the video (leave blank for current directory): ").strip()
    if not path:
        path = "."
    if not os.path.exists(path):
        os.makedirs(path)
    download_youtube_video(url, path)
    print("Download completed successfully!")
