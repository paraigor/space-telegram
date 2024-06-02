from pathlib import Path
from urllib.parse import urlsplit

import requests


def get_ext_from_url(url):
    file_name = urlsplit(url)[2]
    return Path(file_name).suffix


def download_image(link, img_path, payload={}):
    response = requests.get(link, params=payload)
    response.raise_for_status()

    with open(img_path, "wb") as file:
        file.write(response.content)
