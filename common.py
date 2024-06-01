from pathlib import Path
from urllib.parse import urlsplit


def get_ext_from_url(url):
    file_name = urlsplit(url)[2]
    return Path(file_name).suffix
