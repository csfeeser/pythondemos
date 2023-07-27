from flask import Flask
from flask import redirect
from flask import url_for
                    # it finds the url for such-and-such a function

app= Flask(__name__)

# GOAL: no one knows how to spell pokemon!
# people keep typing "pokeman"
# redirect anyone going to "/pokeman" to "/pokemon"

@app.route("/pokemon")
def hello_world():
    return ["bulbasaur","squirtle","charmander"]

@app.route("/pokemon/<trainer>")
def demo(trainer):
    if trainer == "Chad":
        return f"Welcome to the world of Pokemon, Trainer {trainer}!"

    else:
        return redirect(url_for("hello_world"))

app.run(host="0.0.0.0", port=2224)
