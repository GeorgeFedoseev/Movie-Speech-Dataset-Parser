import const

import pysrt
import os

import utils


if __name__ == "__main__":
	inp = os.path.join(const.DATA_DIR, "oceans11.srt")

	srt = pysrt.open(inp, encoding=utils.get_file_encoding(inp))

	out = os.path.join(const.DATA_DIR, "oceans11-utf8.srt")
	srt.save(out, encoding='utf-8')