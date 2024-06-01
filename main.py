import argparse
import configparser
import os
import random
import sys
import time
from pathlib import Path

import telegram
from dotenv import load_dotenv


def get_imgfile_path(name, path):
    for file in path.rglob(name):
        if str(file).endswith(name):
            return file


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    config = configparser.ConfigParser()
    config.read("config.ini")
    pub_freq = config["Telegram"]["PUBLISHING_FREQUENCY"]
    tg_channel_id = config["Telegram"]["CHANNEL_ID"]

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "img_file",
        nargs="?",
        default="rnd",
        help="Specific image file name or 'all' for all downloaded images"
    )
    args = parser.parse_args()

    img_dir = Path("images")
    images = [img for img in img_dir.rglob("*") if img.is_file()]

    tg_bot = telegram.Bot(token=tg_token)

    if args.img_file == "all":
        while True:
            for img in images:
                if img.stat().st_size > 20971520:
                    continue

                tg_bot.send_document(
                    chat_id=tg_channel_id,
                    document=open(img, "rb"),
                )
                time.sleep(float(pub_freq) * 3600)
            random.shuffle(images)
    elif args.img_file == "rnd":
        img_file = random.choice(images)
        if img_file.stat().st_size <= 20971520:
            tg_bot.send_document(
                        chat_id=tg_channel_id,
                        document=open(img_file, "rb"),
                    )
        else:
            sys.exit("Wrong file!")
    else:
        img_file = get_imgfile_path(args.img_file, img_dir)
        if img_file and img_file.stat().st_size <= 20971520:
            tg_bot.send_document(
                        chat_id=tg_channel_id,
                        document=open(img_file, "rb"),
                    )
        else:
            sys.exit("Wrong file!")


if __name__ == "__main__":
    main()
