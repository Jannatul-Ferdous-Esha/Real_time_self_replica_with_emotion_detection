import torch
from tacotron2 import Tacotron2
from waveglow import WaveGlow
from text import text_to_sequence
import soundfile as sf

def synthesize_speech(text, output_path="output.wav"):
    tacotron2 = torch.load('models/tacotron2_model.pt')
    waveglow = torch.load('models/waveglow_model.pt')

    sequence = text_to_sequence(text, ['english_cleaners'])
    sequence = torch.tensor(sequence, dtype=torch.int64).unsqueeze(0)
    mel_outputs, _, _ = tacotron2.inference(sequence)
    audio = waveglow.inference(mel_outputs)

    sf.write(output_path, audio[0].data.cpu().numpy(), 22050)
    return output_path
