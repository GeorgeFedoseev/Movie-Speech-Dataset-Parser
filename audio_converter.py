from cli_dependency_check import is_ffmpeg_installed
import subprocess

def convert_to_wav(in_audio_path, out_audio_path, bitwidth=16, channels=1, samplerate=16000):
    print 'converting %s to wav' % in_audio_path
    p = subprocess.Popen(["ffmpeg", "-y",
         "-i", in_audio_path,         
         "-ac", str(channels),
         "-ab", str(bitwidth),
         "-ar", str(samplerate),
         out_audio_path
         ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, err = p.communicate()

    try:
        p.kill()
    except:
        pass

    if p.returncode != 0:
        print("failed_ffmpeg_conversion "+str(err))
        return False
    return True