#conding:utf-8

import wave
import wav_utils
import os
import const
import subs_utils

import sys

import csv

reload(sys)
sys.setdefaultencoding('utf-8')

def slice(input_audio_path, input_subs_path, output_folder_path, set_id):

    # define paths and ensure folders exist
    set_folder_path = os.path.join(output_folder_path, set_id)
    
    if not os.path.exists(set_folder_path):
        os.makedirs(set_folder_path)

    wav_path = os.path.join(set_folder_path, "audio.wav")

    subs_vtt_path = os.path.join(set_folder_path, "subs.vtt")

    pieces_folder_path = os.path.join(set_folder_path, "pieces/")
    if not os.path.exists(pieces_folder_path):
        os.makedirs(pieces_folder_path)

    pieces_csv_path = os.path.join(set_folder_path, "pieces.csv")

    # convert subs
    if not os.path.exists(subs_vtt_path):
        subs_utils.convert_subs_to_vtt(input_subs_path, subs_vtt_path)

    # get subs
    subs = subs_utils.get_subs(subs_vtt_path)

    # convert audio
    if not os.path.exists(wav_path):
        wav_utils.convert_to_wav(input_audio_path, wav_path)

    # get wave object
    w = wave.open(wav_path, 'r')


    total_speech_bytes = 0

    # open csv
    with open(pieces_csv_path, 'w') as csv_f:        

        for i, s in enumerate(subs):        
            print("process %i/%i" % (i+1, len(subs)))

            if subs_utils.is_bad_subs(s["text"]):
                continue            

            transcript = subs_utils.clean_transcript_text_rus(s["text"])

            # slice audio
            wav_piece_path = os.path.join(pieces_folder_path, "%s-%05i.wav" % (set_id, i) )
            start_ms = int(s["start"]*1000)
            end_ms = int(s["end"]*1000)
            wav_utils.cut_wave(w, wav_piece_path, start_ms, end_ms)

            wav_piece_filesize = os.path.getsize(wav_piece_path)

            total_speech_bytes += wav_piece_filesize


            csv_f.write(wav_piece_path + ", " + str(wav_piece_filesize) + ", " + transcript + "\n")


    print "total speech duration: %.2f hours" % (float(total_speech_bytes)/32000/3600)




        


if __name__ == "__main__":
    audio_path = os.path.join(const.DATA_DIR, "legend.dtshd")
    subs_path = os.path.join(const.DATA_DIR, "legend.srt")

    out_folder_path = const.SPEECH_DATA_DIR

    slice(audio_path, subs_path, out_folder_path, set_id="legend")