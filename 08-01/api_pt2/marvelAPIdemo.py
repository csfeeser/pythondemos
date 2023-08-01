from flask import Flask, render_template, request, make_response, redirect
import json # we now need this tool to convert things in and out of JSON strings


with open("marvel_data.json") as data:
    marvel_characters= json.load(data)


app= Flask(__name__)

def characterlist(hero_choice):

    matches= []

    for char in marvel_characters:
        if char["hero_name"].lower() == hero_choice.lower():
            matches.append(char)

    return matches



@app.route("/")
def start():
    return render_template("index.html")

             # added GET as a viable method for this route
@app.route("/search", methods=["POST", "GET"])
def finder():
  
    if request.method == "GET":
        # check for a cookie, and if we have it, use it
        if request.cookies.get("hero_data"):
            matches= (request.cookies.get("hero_data"))
            print(matches)
            print(type(matches))
            matches= json.loads(matches)
            print(matches)
            # ^ contains the matched heroes we grabbed last, convert back to list

            return render_template("display.html", characters= matches)
        else:
            # if a user didn't have a "hero_data" cookie, let's send them back to the main page search
            return redirect("/")


    if request.method == "POST":
        if request.form.get("nm"):
            choice= request.form.get("nm")
            matches= characterlist(choice)

            # HOW TO COOKIE:
            # 1. create a response BUT DON'T SEND IT
            response= make_response(render_template("display.html", characters= matches))

            # 2. set a cookie value in the response- remember only strings can be in cookies!
            # we are converting a JSON string so that it can be easily converted back into a python list later!
            response.set_cookie("hero_data", json.dumps(matches))

            # 3. send the response to the client
            return response
        
        else:
            return []


@app.route("/all")
def all():
    """returns all data on all characters"""
    return marvel_characters

@app.route("/search/<hero_choice>")
def specifichero(hero_choice):
    """takes a chosen hero from the URL and returns a matching hero data (if it exists)"""

    matches= characterlist(hero_choice)

    return matches

@app.route("/abilities")
def justtheabilities():
    """displays all the characters' abilities in a single list"""

    ability_list= []

    for char in marvel_characters:
        ability_list.extend(char["abilities"])

    ability_list= set(ability_list)
    ability_list= list(ability_list)

    return ability_list

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)
