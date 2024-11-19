from synthesizer import Synthesizer
from encoder import inference as encoder
from vocoder import inference as vocoder
import soundfile as sf

def clone_voice(original_voice_path, text, output_path="cloned_voice.wav"):
    encoder.load_model("models/encoder/saved_models")
    synthesizer = Synthesizer("models/synthesizer/saved_models")
    vocoder.load_model("models/vocoder/saved_models")

    embed = encoder.embed_utterance(encoder.preprocess_wav(original_voice_path))
    spectrogram = synthesizer.synthesize_spectrograms([text], [embed])[0]
    generated_wav = vocoder.infer_waveform(spectrogram)

    sf.write(output_path, generated_wav, synthesizer.sample_rate)
    return output_path
