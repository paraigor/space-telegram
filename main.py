import argparse
import configparser
import os
import random
import time
from pathlib import Path

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    config = configparser.ConfigParser()
    config.read("config.ini")
    pub_freq = config["Telegram"]["PUBLISHING_FREQUENCY"]
    tg_channel_id = config["Telegram"]["CHANNEL_ID"]

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "publishing_frequency",
        nargs="?",
        default=pub_freq,
        help=f"Publishing frequency in hours, default {pub_freq}",
    )
    args = parser.parse_args()

    img_dir = Path("images")
    images = [img for img in img_dir.rglob("*") if img.is_file()]

    tg_bot = telegram.Bot(token=tg_token)

    while True:
        for img in images:
            if img.stat().st_size > 20971520:
                continue

            tg_bot.send_document(
                chat_id=tg_channel_id,
                document=open(img, "rb"),
            )
            time.sleep(float(args.publishing_frequency) * 3600)

        random.shuffle(images)


if __name__ == "__main__":
    main()
