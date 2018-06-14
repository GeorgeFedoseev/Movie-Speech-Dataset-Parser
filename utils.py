import chardet

def get_file_encoding(path):
	with open(path, "r") as f:
		text = f.read()
		res = chardet.detect(text)
		return res["encoding"]