import os
import audio_converter
import const

if __name__ == "__main__":
    inp = os.path.join(const.DATA_DIR, "oceans11.ac3")
    out = os.path.join(const.DATA_DIR, "oceans11.wav")
    audio_converter.convert_to_wav(inp, out)