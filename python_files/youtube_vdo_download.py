from pytube import YouTube

def download_youtube_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.filter(res="720p").first()

        if not video_stream:
            print("720p stream not available. Downloading the best available stream.")
            video_stream = yt.streams.get_highest_resolution()
            
        video_stream.download(output_path)
        print("Download completed successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=WTdziAshzoE"
    output_path = "./downloads"

    download_youtube_video(video_url, output_path)
