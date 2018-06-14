# coding:utf-8

import subs_utils
import os
import const
import io

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":

	inp = os.path.join(const.DATA_DIR, "oceans11.srt")

	out = os.path.join(const.DATA_DIR, "oceans11.vtt")

	subs_utils.convert_subs_to_vtt(inp, out)

	subs = subs_utils.get_subs(out)