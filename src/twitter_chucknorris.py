import os
import random
import sys
import requests
import tweepy


def get_joke_icndb() -> str:
    """Get Chuck Norris joke from icndb.com

    :return: joke
    :rtype: str
    """
    data = get_from_url("http://api.icndb.com/jokes/random?escape=javascript")

    if data["type"] != "success":
        sys.exit(f'Response "type" from ICNDB not "success"\n{data}')

    return data["value"]["joke"]


def get_joke_cnio() -> str:
    """Get Chuck Norris joke from chucknorris.io

    :return: joke
    :rtype: str
    """
    data = get_from_url("https://api.chucknorris.io/jokes/random")
    return data["value"]


def get_from_url(url: str) -> requests.structures.LookupDict:
    """Get JSON from API endpoint and raise exception if status code is not OK

    :param url: URL
    :type url: str
    :return: JSON from URL
    :rtype: requests.structures.LookupDict
    """
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def setup_twitter_api() -> tweepy.API:
    """Setup tweepy API instance from environment variables

    :return: tweepy API instance
    :rtype: tweepy.API
    """
    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.verify_credentials()
    return api


def lambda_handler(event, context):
    joke = get_joke_icndb() if random.choice((True, False)) else get_joke_cnio()

    api = setup_twitter_api()
    api.update_status(joke)