import argparse
from pathlib import Path

import requests

from common import download_image, get_ext_from_url


def fetch_spacex_launch(launch_id):
    img_folder = Path("images/spacex")
    img_folder.mkdir(parents=True, exist_ok=True)

    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()["links"]["flickr"]["original"]

    for number, img_link in enumerate(images):
        img_filename = f"spacex{number:03}{get_ext_from_url(img_link)}"
        img_path = img_folder.joinpath(img_filename)
        download_image(img_link, img_path)


def main():
    parser = argparse.ArgumentParser(
        description="""Script for downloading images from SpaceX
                         shuttles launches"""
    )
    parser.add_argument(
        "launch_id",
        nargs="?",
        default="latest",
        help="ID of set of images, default 'latest'",
    )
    args = parser.parse_args()
    fetch_spacex_launch(args.launch_id)


if __name__ == "__main__":
    main()
