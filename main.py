from video_capture import capture_video
from face_animation import animate_face
from speech_synthesis import synthesize_speech
from voice_cloning import clone_voice
from nlp_processing import generate_text
from integration import combine_audio_video

def main():
    # Step 1: Capture video
    driving_video_path = capture_video()

    # Step 2: Animate face
    source_image_path = "path/to/source_image.png"  # Replace with your actual image path
    animated_video_path = animate_face(source_image_path, driving_video_path)

    # Step 3: NLP processing (generate text)
    input_text = "How are you?"
    generated_text = generate_text(input_text)

    # Step 4: Speech synthesis
    synthesized_audio_path = synthesize_speech(generated_text)

    # Step 5: Voice cloning (if needed)
    original_voice_path = "path/to/voice_sample.wav"  # Replace with your actual voice sample path
    cloned_voice_path = clone_voice(original_voice_path, generated_text)

    # Step 6: Integration
    final_output_path = combine_audio_video(animated_video_path, cloned_voice_path)

    print(f"Final output saved at: {final_output_path}")

if __name__ == "__main__":
    main()
