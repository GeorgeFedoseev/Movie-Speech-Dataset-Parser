# coding:utf-8

from pycaption import WebVTTWriter, SRTReader
import os
import const
import io

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":

	inp = os.path.join(const.DATA_DIR, "oceans11-utf8.srt")
	with open(inp, 'r') as f:
		subs = SRTReader().read(f.read().decode('utf-8'))

		print WebVTTWriter().write(subs)
