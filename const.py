import os

DATA_DIR = os.path.join(os.getcwd(), "data")
TORRENT_DOWNLOAD_DIR = os.path.join(DATA_DIR, "torrent_downloads")
SPEECH_DATA_DIR = os.path.join(DATA_DIR, "speech_data")
DOWNLOADS_DIR = os.path.join(DATA_DIR, "downloads")


def ensure_main_folders_created():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(TORRENT_DOWNLOAD_DIR):
        os.makedirs(TORRENT_DOWNLOAD_DIR)

    if not os.path.exists(SPEECH_DATA_DIR):
        os.makedirs(SPEECH_DATA_DIR)

    if not os.path.exists(DOWNLOADS_DIR):
        os.makedirs(DOWNLOADS_DIR)



if __name__ == "__main__":
    ensure_main_folders_created()