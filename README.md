# Chuck Norris Bot
This is a Twitter bot that posts Chuck Norris jokes on a schedule. It is made to be scheduled to be run by cron, and it uses Twitter's API. To install it yourself, follow the instructions below.

## Installation

1. `pip install -r requirements.txt # Install dependencies`
2. `cp example_config.py config.py # Create config file`
3. Add your Twitter API credentials to config.py

## Usage

- To run once: `python3 main.py`
- To run daily add this to your crontab: `30 12 * * * python3 /<path>/<to>/<repo>/main.py # Run bot daily at 12:30 pm`

## Profit??