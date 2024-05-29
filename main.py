import os
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

import requests
from dotenv import load_dotenv


def fetch_spacex_last_launch(id):
    img_folder = Path("spacex")
    img_folder.mkdir(exist_ok=True)

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
        link = item["url"]
        img_filename = f"nasa{num:03}{get_ext_from_url(link)}"
        img_path = img_folder.joinpath(img_filename)
        response = requests.get(link)
        response.raise_for_status()

        with open(img_path, "wb") as file:
            file.write(response.content)


def fetch_nasa_epic(token, n):
    img_folder = Path("nasa")
    img_folder.mkdir(exist_ok=True)

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


def get_ext_from_url(url):
    file_name = urlsplit(url)[2]
    return Path(file_name).suffix


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_API_TOKEN"]
    spacex_launch_id = "5eb87d46ffd86e000604b388"
    number_of_nasa_apod_images = 30
    number_of_nasa_epic_images = 5

    fetch_spacex_last_launch(spacex_launch_id)
    fetch_nasa_apod(nasa_token, number_of_nasa_apod_images)
    fetch_nasa_epic(nasa_token, number_of_nasa_epic_images)


if __name__ == "__main__":
    main()
