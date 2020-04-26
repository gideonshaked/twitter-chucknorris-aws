# Chuck Norris Bot
This is a Twitter bot that posts Chuck Norris jokes on a schedule. It is made to be scheduled to be run by cron, and it uses Twitter's API. To install it yourself, follow the instructions below.

## Installation

1. `cp example_config.py config.py # Create config file`
2. Add your Twitter API credentials to config.py
3. `pipenv install # Install dependencies`

## Usage

Add this to your cron file: `30 12 * * * pipenv run python /path/to/repo/main.py # This runs the bot at 12:30 pm every day`

## Profit??
