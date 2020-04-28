# Chuck Norris Bot [![Build Status](https://travis-ci.com/The-Kid-Gid/Chuck-Norris-Bot.svg?branch=master)](https://travis-ci.com/The-Kid-Gid/Chuck-Norris-Bot)

This is a Twitter bot that posts Chuck Norris jokes on a schedule. It is intended to be run on a schedule by cron, and it uses Twitter's API. To install it yourself, follow the instructions below.

## Installation

`sudo python3 -m pip install -r requirements.txt # Install dependencies`

## Config

1. `cp example_config.ini config.ini # Create config file`
2. Add your Twitter API credentials to config.ini.

## Usage

- To run once: `python3 main.py`
- To run daily add this to your crontab: `30 12 * * * python3 /<path>/<to>/<repo>/main.py # Run bot daily at 12:30 pm`
