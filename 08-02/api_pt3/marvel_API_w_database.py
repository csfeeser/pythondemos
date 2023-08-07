from flask import Flask, render_template, request, make_response, redirect
import json

#with open("marvel_data.json") as data:
#    marvel_characters= json.load(data)

app= Flask(__name__)

def characterlist(hero_choice):
    """takes a hero name, returns a list of characters who match"""
    matches= []
    for char in marvel_characters:
        if char["hero_name"].lower() == hero_choice.lower():
            matches.append(char)
    return matches

@app.route("/")
def start():
    """landing page, returns HTML asking for a hero name"""
    return render_template("index.html")

@app.route("/search", methods=["POST", "GET"])
def finder():
    """checks for requested hero, returns page with hero data displayed in html"""
    if request.method == "GET":
        if request.cookies.get("hero_data"):
            matches= (request.cookies.get("hero_data"))
            print(matches)
            print(type(matches))
            matches= json.loads(matches)
            print(matches)
            return render_template("display.html", characters= matches)
        else:
            return redirect("/")

    if request.method == "POST":
        if request.form.get("nm"):
            choice= request.form.get("nm")
            matches= characterlist(choice)
            response= make_response(render_template("display.html", characters= matches))
            response.set_cookie("hero_data", json.dumps(matches))
            return response
        
        else:
            return []

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)
