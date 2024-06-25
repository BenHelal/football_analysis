from pytube import YouTube

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video
        stream.download(output_path)
        
        print(f"Video downloaded successfully to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=DYKespAlxH0'
    output_path = 'input_videos'
    
    download_video(video_url, output_path)
