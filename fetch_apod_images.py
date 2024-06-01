import argparse
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

from common import get_ext_from_url


def fetch_nasa_apod(token, n):
    img_folder = Path("nasa")
    img_folder.mkdir(exist_ok=True)

    payload = {
        "api_key": token,
        "count": n,
    }
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images = response.json()

    for num, item in enumerate(images):
        if item["media_type"] != "image":
            continue

        link = item["url"]
        img_filename = f"nasa{num:03}{get_ext_from_url(link)}"
        img_path = img_folder.joinpath(img_filename)
        try:
            response = requests.get(link)
            response.raise_for_status()
        except requests.HTTPError:
            continue

        with open(img_path, "wb") as file:
            file.write(response.content)


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_API_TOKEN"]

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "n",
        nargs="?",
        default="3",
        help="Number of images to fetch, default 3",
    )
    args = parser.parse_args()

    fetch_nasa_apod(nasa_token, int(args.n))


if __name__ == "__main__":
    main()
