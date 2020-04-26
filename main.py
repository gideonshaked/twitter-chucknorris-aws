
import requests
import json
import sys
from datetime import datetime
import random

def getJoke1():
    response = requests.get("http://api.icndb.com/jokes/random?escape=javascript")

    if (response.status_code != 200):
        logError("Status code returned from icndb.com not 200. Status code " + response.status_code)

    data = response.json()

    if (data["type"] != "success"):
        logError("JSON \"type\" from ICNDB not success. Returned \"type\" " + data["type"])

    joke = data["value"]["joke"]
    return joke

def getJoke2():
    response = requests.get("https://api.chucknorris.io/jokes/random")

    if (response.status_code != 200):
        logError("Status code returned from chucknorris.io not 200. Status code " + response.status_code)

    data = response.json()
    joke = data["value"]
    return joke

def logError(error):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = open("errors.log", "w")
    log.write(time + ": " + error)
    log.close()
    sys.exit()

def main():
    if (random.randint(0,1) % 2 == 0):
        joke = getJoke1()
    else:
        joke = getJoke2()

    print(joke)

if __name__ == '__main__':
    main()