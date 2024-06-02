import argparse
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

from common import download_image, get_ext_from_url


def fetch_nasa_apod(token, qty):
    img_folder = Path("images/nasa")
    img_folder.mkdir(parents=True, exist_ok=True)

    payload = {
        "api_key": token,
        "count": qty,
    }
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images = response.json()

    for i, img_link in enumerate(images):
        if img_link["media_type"] != "image":
            continue

        link = img_link["url"]
        img_filename = f"nasa{i:03}{get_ext_from_url(link)}"
        img_path = img_folder.joinpath(img_filename)
        try:
            download_image(link, img_path)
        except requests.exceptions.HTTPError:
            continue


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_API_TOKEN"]

    parser = argparse.ArgumentParser(
        description="""Script for downloading images from NASA Astronomy
                         Picture of the Day Archive"""
        )
    parser.add_argument(
        "n",
        type=int,
        nargs="?",
        default=3,
        help="Number of images to fetch, default 3",
    )
    args = parser.parse_args()

    fetch_nasa_apod(nasa_token, args.n)


if __name__ == "__main__":
    main()
