from cli_dependency_check import is_ffmpeg_installed
import subprocess


def convert_to_wav(in_audio_path, out_audio_path, bitwidth=16, channels=1, samplerate=16000):
    print 'converting %s to wav' % in_audio_path

    if not is_ffmpeg_installed():
        return


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


def is_bad_piece(audio_duration, transcript):   

    MAX_SECS = 20
    MIN_SECS = 3    
    
    MIN_SEC_PER_SYMBOL = 0.03
    #MIN_SEC_PER_SYMBOL = 0

    # remove audios that are shorter than 0.5s and longer than 20s.
    # remove audios that are too short for transcript.
    if audio_duration > MIN_SECS and audio_duration < MAX_SECS and transcript!="" and audio_duration/len(transcript) > MIN_SEC_PER_SYMBOL:
        return False
    return True