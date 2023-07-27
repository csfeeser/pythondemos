#!/usr/bin/python3
import requests
import argparse

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    print(f"Welcome, {args.name}! Let's get crackin' with your API!")
    nasacreds = "api_key=" + args.key # API KEY GOES HERE
    url= NASAAPI + nasacreds
    print(url)
    apodresp = requests.get(url)
    apod = apodresp.json()

    print("YOUR IMAGE URL:", apod["url"])

# BEFORE MAIN RUNS
parser= argparse.ArgumentParser(description="Collects an API key to access a NASA API.")
            # ^ custom class object
            # creating an object that scoops up
            # our little --args at the command line

parser.add_argument("--name", help="The user's name", default="Slappy")
# teach our lil' parser object the different arguments that our code will take!
parser.add_argument("--key", required=True, help="NASA API key string")
                             # ^ you MUST use this arg!

# have the parser combine all those arguments into one object
args= parser.parse_args()

main()



