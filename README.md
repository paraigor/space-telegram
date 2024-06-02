# Space Telegram

A set of scripts for downloading various images from NASA database, using NASA Open APIs, SpaceX database, and automatically publishing them to Telegram channel.

### Installation

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

NASA API key is required to use scripts. Key can be generated on [NASA API website](https://api.nasa.gov/) and looks like: `a3aOIO75GG1pxMXMI9wqs7X9jXTLxxbLTgfx75X5`.

Security sensitive information recommended storing in the project using `.env` files.

Key name to store token value is `NASA_API_TOKEN`.

Telegram bot and channel (group) also needed for images publishing. Create bot via [@BotFather](https://t.me/BotFather). Bot token looks like: `1234567890:XXXxx0Xxx-xxxX0xXXxXxx0X0XX0XXXXxXx`.

Key name to store bot API token value is `TG_TOKEN`.

Set Telegram channel ID in `config.ini`:
```
[Telegram]
CHANNEL_ID = @chat_id
```

Also publish frequency to Telegram channel, SpaceX launch ID and numbers of NASA images to download can be modified in `config.ini` or left defaults.
```
[NASA images]
SPACEX_LAUNCH_ID = 5eb87d46ffd86e000604b388
NUMBER_OF_NASA_APOD_IMAGES = 30
NUMBER_OF_NASA_EPIC_IMAGES = 5

[Telegram]
PUBLISHING_FREQUENCY = 4
```

### Usage

#### tg_img_publish.py

Script is used for automated publishing of downloaded images to Telegram channel.  
Pass specific image file name or 'all' for all downloaded images as an argument:
```
python tg_img_publish.py nasa001.jpg
python tg_img_publish.py all
```
If no arguments provided, one random image will be published.

#### fetch_apod_images.py

Script is used for downloading images from NASA Astronomy Picture of the Day Archive.  
Number of desired images can be passed as an argument:
```
python fetch_apod_images.py 30
```

#### fetch_epic_images.py

Script is used for downloading images of our planet from NASA EPIC Archive.  
Number of desired images can be passed as an argument:
```
python fetch_epic_images.py 5
```

#### fetch_spacex_images.py

Script is used for downloading images from SpaceX shuttles launches.  
Launch ID can be passed as an argument:
```
python fetch_spacex_images.py 5eb87d46ffd86e000604b388
```
Otherwise images from last launch will be downloaded.

#### fetch_all_images.py
This script can be used to download all images at ones, using preset values from `config.ini`.

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/). 
 
