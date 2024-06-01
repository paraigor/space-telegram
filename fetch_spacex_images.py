import argparse
from pathlib import Path

import requests

from common import get_ext_from_url


def fetch_spacex_launch(id):
    img_folder = Path("images/spacex")
    img_folder.mkdir(parents=True, exist_ok=True)

    url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()["links"]["flickr"]["original"]

    for num, link in enumerate(images):
        img_filename = f"spacex{num:03}{get_ext_from_url(link)}"
        img_path = img_folder.joinpath(img_filename)
        response = requests.get(link)
        response.raise_for_status()

        with open(img_path, "wb") as file:
            file.write(response.content)


def main():
    parser = argparse.ArgumentParser()
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
