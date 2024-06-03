import argparse
import os
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

from common import download_image


def fetch_nasa_epic(token, qty):
    img_folder = Path("images/nasa")
    img_folder.mkdir(parents=True, exist_ok=True)

    payload = {"api_key": token}
    request_url = "https://api.nasa.gov/EPIC/api/natural/images/"
    response = requests.get(request_url, params=payload)
    response.raise_for_status()
    images = response.json()

    for number, image in enumerate(images[:qty]):
        img_name = image["image"]
        img_date = datetime.strptime(image["date"], "%Y-%m-%d %H:%M:%S")
        img_url = "https://api.nasa.gov/EPIC/archive/natural/"
        img_url += f"{img_date.year}/{img_date.month:02}/{img_date.day:02}"
        img_url += f"/png/{img_name}.png"

        img_filename = f"nasa_epic{number:03}.png"
        img_path = img_folder.joinpath(img_filename)
        download_image(img_url, img_path, payload=payload)


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_API_TOKEN"]

    parser = argparse.ArgumentParser(
        description="""Script for downloading images of our planet from
                         NASA EPIC Archive"""
        )
    parser.add_argument(
        "n",
        type=int,
        nargs="?",
        default=3,
        help="Number of images to fetch, default 3",
    )
    args = parser.parse_args()

    fetch_nasa_epic(nasa_token, args.n)


if __name__ == "__main__":
    main()
