import moviepy.editor as mp

def extract_audio_and_remove_audio(input_video_path, output_audio_path, output_video_path):
    video_clip = mp.VideoFileClip(input_video_path)                             # Load the video clip

    audio_clip = video_clip.audio                                               # Extract audio from the video clip
    audio_clip.write_audiofile(output_audio_path)                               # Save the extracted audio as an audio file (e.g., in MP3 format)
    video_clip = video_clip.set_audio(None)                                     # Remove audio from the video clip
    video_clip.write_videofile(output_video_path, codec='libx264')              # Save the video without audio

    video_clip.close()
    audio_clip.close()

if __name__ == "__main__":
    input_video_path = "input_video.mp4"
    output_audio_path = "output_audio.mp3"
    output_video_path = "output_video_without_audio.mp4"

    extract_audio_and_remove_audio(input_video_path, output_audio_path, output_video_path)
