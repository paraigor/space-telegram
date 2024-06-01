import os
import random
from pathlib import Path

import telegram
from dotenv import load_dotenv

from fetch_apod_images import fetch_nasa_apod
from fetch_epic_images import fetch_nasa_epic
from fetch_spacex_images import fetch_spacex_launch


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_API_TOKEN"]
    tg_token = os.environ["TG_TOKEN"]

    spacex_launch_id = "5eb87d46ffd86e000604b388"
    number_of_nasa_apod_images = 30
    number_of_nasa_epic_images = 5

    fetch_spacex_launch(spacex_launch_id)
    fetch_nasa_apod(nasa_token, number_of_nasa_apod_images)
    fetch_nasa_epic(nasa_token, number_of_nasa_epic_images)

    img_dir = Path("images")
    images = [img for img in img_dir.rglob("*") if img.is_file()]

    tg_bot = telegram.Bot(token=tg_token)
    tg_bot.send_document(
        chat_id="@skir_space_photos",
        document=open(random.choice(images), "rb"),
    )


if __name__ == "__main__":
    main()
