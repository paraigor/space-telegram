import argparse
import os
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv


def fetch_nasa_epic(token, n):
    img_folder = Path("images/nasa")
    img_folder.mkdir(parents=True, exist_ok=True)

    payload = {"api_key": token}
    request_url = "https://api.nasa.gov/EPIC/api/natural/images/"
    response = requests.get(request_url, params=payload)
    response.raise_for_status()
    images = response.json()

    for num, item in enumerate(images[:n]):
        img_name = item["image"]
        img_date = datetime.strptime(item["date"], "%Y-%m-%d %H:%M:%S")
        img_url = "https://api.nasa.gov/EPIC/archive/natural/"
        img_url += f"{img_date.year}/{img_date.month:02}/{img_date.day}"
        img_url += f"/png/{img_name}.png"

        img_filename = f"nasa_epic{num:03}.png"
        img_path = img_folder.joinpath(img_filename)
        response = requests.get(img_url, params=payload)
        response.raise_for_status()

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

    fetch_nasa_epic(nasa_token, int(args.n))


if __name__ == "__main__":
    main()
