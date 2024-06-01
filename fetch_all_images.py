import configparser
import os

from dotenv import load_dotenv

from fetch_apod_images import fetch_nasa_apod
from fetch_epic_images import fetch_nasa_epic
from fetch_spacex_images import fetch_spacex_launch


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_API_TOKEN"]
    config = configparser.ConfigParser()
    config.read("config.ini")

    spacex_launch_id = config["NASA images"]["SPACEX_LAUNCH_ID"]
    number_of_apod_images = config["NASA images"]["NUMBER_OF_NASA_APOD_IMAGES"]
    number_of_epic_images = config["NASA images"]["NUMBER_OF_NASA_EPIC_IMAGES"]

    fetch_spacex_launch(spacex_launch_id)
    fetch_nasa_apod(nasa_token, int(number_of_apod_images))
    fetch_nasa_epic(nasa_token, int(number_of_epic_images))


if __name__ == "__main__":
    main()
