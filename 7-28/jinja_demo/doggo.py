# Pet Adoption Website!

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

cool_peep= "Chad"
pets_for_sale= ["dog","cat","moose","elk"]

@app.route("/")
def landing():
    return render_template("pets.html", 
                           honkalonkadingdong=cool_peep,
                           critter_list= pets_for_sale
                          )

# add a new pet for adoption
@app.route("/sammyscoolcritteremporium", methods=["POST"])
def grabnewcritter():
    # grab the name of the new animal
    # add that name to the list above
    animal_name= request.form.get("SAMMYS_COOL_VAR") # <-- grab the value of a variable off a FORM

    # animal_name = mouse or whatever the user typed in
    pets_for_sale.append(animal_name)

    # every route must ALWAYS return something!
    return redirect("/")



app.run(host="0.0.0.0", port=2224, debug=True)
