# coding:utf-8

from pycaption import WebVTTWriter, WebVTTReader, SRTReader, detect_format
import utils
import pyvtt
import re


def convert_subs_to_vtt(input_subs_path, output_vtt_path):
    with open(input_subs_path, 'r') as f:
            text = f.read().decode(utils.get_file_encoding(input_subs_path))
            reader = detect_format(text)
            subs = reader().read(text)

            output_text = WebVTTWriter().write(subs)

            with open(output_vtt_path, 'w') as w:
                w.write(output_text)


def get_subs(vtt_subs_path):
    subs = []

    reader = WebVTTReader()

    with open(vtt_subs_path, 'r') as f:
        text = f.read().decode(utils.get_file_encoding(vtt_subs_path))
        vtt = reader.read(text)

        vttsubs = vtt.get_captions(vtt.get_languages()[0])
        #vttsubs = pyvtt.WebVTTFile.open(vtt_subs_path)

        print "vttsubs total: %i " % len(vttsubs)

        print vttsubs[0].start
        print vttsubs[0].end
        print vttsubs[0].get_text()

        for s in vttsubs:
            subs.append({
            "text": s.get_text(),
            "start": float(s.start)/1000000,
            "end": float(s.end)/1000000
        })

        return subs




def is_bad_subs(subs_text):
    bad = False

    if subs_text.strip() == "":
        bad = True

    if len(re.findall(r'[0-9]+', subs_text)) > 0:
        bad = True
    if len(re.findall(r'[A-Za-z]+', subs_text)) > 0:
        bad = True

    return bad

def clean_transcript_text_rus(transcript):
    transcript = re.sub(r'<[^>]*>', '', transcript)
    transcript = transcript.replace("\n", " ")
    transcript = re.sub(u'[^а-яё\- ]', '', transcript.strip().lower()).strip()
    transcript = transcript.replace("ё", "е")

    return transcript
