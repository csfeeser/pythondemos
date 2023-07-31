from flask import Flask, render_template, request
import json # need this so we can read in a JSON file of marvel characters


# these two lines open the json file containing all our hero data
# it then saves a list of character dictionaries as the variable "marvel_characters"
with open("marvel_data.json") as data:
    marvel_characters= json.load(data)


app= Flask(__name__)

def characterlist(hero_choice):

    matches= []

    # loop over the list of characters
    for char in marvel_characters:
        # see if the character's name matches the chosen character
        if char["hero_name"].lower() == hero_choice.lower():
            # when a match is found, add that character's dictionary to the list
            matches.append(char)

    # this function will spit back (return) a list of matching characters
    return matches



@app.route("/")
def start():
    return render_template("index.html")

             # routes will accept GET by default
             # if you want to allow anything else (POST)
@app.route("/search", methods=["POST"])
def finder():
    
    # check if the user actually chose a hero
    if request.form.get("nm"):
        # if there was a hero, set it as a var
        choice= request.form.get("nm")
        # example: choice = "thor"
    
                 # pass our choice of hero into the characterlist function;
                 # it will return back a list of character matches
        matches= characterlist(choice)
        # matches = list of character dictionaries


        # the jinja in display.html needs a variable called "characters" to be defined
        # so we will pass our "matches" list in as the variable "characters" in display.html
        return render_template("display.html", characters= matches)

    
    else:
        return []

    # read off the data inside of the form
    # use that data to find matching heroes
    # return those matching to user
    # ^ as jinja template?
    
    return matching_heroes






@app.route("/all")
def all():
    """returns all data on all characters"""
    # returns the full data value we created above
    return marvel_characters

@app.route("/<hero_choice>")
def specifichero(hero_choice):
    """takes a chosen hero from the URL and returns a matching hero data (if it exists)"""

    # this list is empty, we will add matching characters to it later
    matches= characterlist(hero_choice)

    # return the list of all matches to the client
    return matches

@app.route("/abilities")
def justtheabilities():
    """displays all the characters' abilities in a single list"""

    # start with an empty list, we'll add to it later
    ability_list= []

    # loop over the list of characters
    for char in marvel_characters:
        # grab each character's list of abilities and combine it with our list above
        ability_list.extend(char["abilities"])

    # oops! some heroes have the same powers so we have duplicates.
    # to fix we convert the list to a set (sets can't have duplicate values)
    ability_list= set(ability_list)

    # then we convert it back to a list
    ability_list= list(ability_list)

    # return the finished product to the client
    return ability_list




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)
