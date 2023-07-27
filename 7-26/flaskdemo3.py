from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request

app= Flask(__name__)

# allow users to POST new pokemon!

pokedex= ["bulbasaur","squirtle","charmander"]

@app.route("/")
def showmedathtml():
    return render_template("postmaker.html")
                            # ^^^ did not mention this is in a folder named "templates"


@app.route("/login", methods=["POST"])
def addnew():
    # request() function can do is that it can suck data out
    # of incoming requests

    newpokemon= request.form["nm"]  # nm = whatever we typed into that field box

    if newpokemon: # check if a pokemon name was actually given!
        pokedex.append(newpokemon)

    return pokedex














app.run(host="0.0.0.0", port=2224)
