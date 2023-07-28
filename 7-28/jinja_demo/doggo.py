# Pet Adoption Website!

from flask import Flask
from flask import render_template

app = Flask(__name__)

cool_peep= "Chad"
pets_for_sale= ["dog","cat","hamster","lizard", "mouse", "bird", "pterodactyl"]

specific_pets= [
                {"species": "dog",
                 "name"   : "Spot",
                 "favfood" : "jerky"},
                {"species": "cat",
                 "name"   : "Beefalo",
                 "favfood": "fish"},
                {"species": "hamster",
                 "name"   : "Hercules",
                 "favfood": "fingers"}
                ]

@app.route("/")
def landing():
    return render_template("pets.html", 
                           honkalonkadingdong=cool_peep,
                           critter_list= pets_for_sale
                          )

app.run(host="0.0.0.0", port=2224, debug=True)
