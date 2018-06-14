from cli_dependency_check import is_aria2c_installed
import subprocess

def download_torrent_with_torrent_file(torrent_file_path, download_dir):
    if not is_aria2c_installed:
        raise Exception("CLI Torrent client aria2c is not installed")

    p = subprocess.Popen(["aria2c", 
        "-d", download_dir, 
        "--seed-time", "0",
        torrent_file_path
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, err = p.communicate()

    if p.returncode != 0:
        raise Exception("Failed to loudnorm: %s" % str(err))
    pass