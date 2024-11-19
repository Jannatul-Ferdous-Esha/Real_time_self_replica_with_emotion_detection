import moviepy.editor as mp

def combine_audio_video(video_path, audio_path, output_path="final_output.mp4"):
    video = mp.VideoFileClip(video_path)
    audio = mp.AudioFileClip(audio_path)

    final_video = video.set_audio(audio)
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path
print(mp.__version__)