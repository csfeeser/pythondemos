import requests

answer= input("Would you like to see Gen1 or Gen2 pokemon?")

if answer == "1":
    query= "?limit=151"

elif answer == "2":
    query= "?limit=100&offset=151"

else:
    query= "?offset=251&limit=100"

url= "https://pokeapi.co/api/v2/pokemon" + query

data= requests.get(url).json()

for poke in data["results"]:
    # looping over the list of pokemon
    if poke["name"].startswith("g"):
        # use the "if" as a filter
        print(poke["name"])


# return only pokemon whose names start with "G"


