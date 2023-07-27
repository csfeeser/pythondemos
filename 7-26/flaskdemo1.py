# only going to import a PIECE of the flask library
from flask import Flask

                 # ^ custom class object!

# Flask == to app we are about to build!

# app is the variable that represents our website that we are building!
# we are going to "teach" our lil app object how we want it to behave!
app= Flask(__name__)

# GOAL:
# add a page to my website that displays the message "hello world"

# DECORATORS- add additional functionality to the function that they are "decorating"
@app.route("/pokemon")
def hello_world():
    return ["bulbasaur","squirtle","charmander"]


@app.route("/pokemon/<trainer>")
def demo(trainer):
    return f"Welcome to the world of Pokemon, Trainer {trainer}!"

# start our web application running!
app.run(host="0.0.0.0", port=2224)
