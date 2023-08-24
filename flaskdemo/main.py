from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for # looks up whatever the url is for one of the functions
from flask import request

app = Flask(__name__)

# Chinese Zodiac Horoscopes
chinese_zodiac_horoscopes = {
    "Rat": "A year of unexpected opportunities awaits you.",
    "Ox": "Persistence and hard work will pay off.",
    "Tiger": "Embrace change and take bold steps.",
    "Rabbit": "A peaceful year filled with happiness.",
    "Dragon": "Your ambitious plans will come to fruition.",
    "Snake": "Wisdom and growth will guide your path.",
    "Horse": "Adventure and travel are on the horizon.",
    "Goat": "A creative year; trust your artistic instincts.",
    "Monkey": "Use your wit and intelligence to solve problems.",
    "Rooster": "A year to stand tall and embrace leadership.",
    "Dog": "Loyalty and friendships will enrich your life.",
    "Pig": "Enjoy the pleasures and embrace joy."
}

# Traditional (Western) Zodiac Horoscopes
western_zodiac_horoscopes = {
    "Aries": "A year of action and determination.",
    "Taurus": "Steadiness will lead to success.",
    "Gemini": "Embrace both sides of your personality.",
    "Cancer": "A year of deep emotions and family connections.",
    "Leo": "Shine brightly and take the center stage.",
    "Virgo": "A detail-oriented approach will be rewarded.",
    "Libra": "Balance and harmony will guide you.",
    "Scorpio": "Intense passions will drive your actions.",
    "Sagittarius": "Explore new horizons and seek wisdom.",
    "Capricorn": "Practicality and planning will be your guide.",
    "Aquarius": "Innovation and uniqueness will be celebrated.",
    "Pisces": "A spiritual journey will lead to self-discovery."
}

def chinese_zodiac_animal(birth_year):
    """takes incoming birth year and returns animal of chinese zodiac"""
    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    return animals[(birth_year - 4) % 12]

@app.route("/")
def start():
    """this is the landing page; it will prompt a user to enter their name and select their sign"""
    return render_template("index.html")

@app.route("/horoscope", methods=["POST"])
def horoscope():
    """this will return jinja2 html that contains horoscope info"""
    if request.form.get("birth_year"):
        year= int(request.form.get("birth_year"))

        # want to debug and see if "year" is actually an integer
        print(type(year))

    else:
        return redirect("/")  # didn't give me a birth year? BACK TO THE FORM

    if request.form.get("astrological_sign"):
        sign= request.form.get("astrological_sign").title()
    else:
        return redirect("/")  # didn't give me a sign? BACK TO THE FORM

    if request.form.get("nm"):
        name= request.form.get("nm")
    else:
        return redirect("/")  # didn't give me a name? BACK TO THE FORM

    # var represents the appropriate chinese zodiac animal
    chinese_zodiac= chinese_zodiac_animal(year)

    #return f"{name} {year} {sign} {chinese_zodiac}"

    # dict

    return render_template("horoscope.html.j2", name=name, year=year, sign=sign, animal=chinese_zodiac, eastern=chinese_zodiac_horoscopes, western=western_zodiac_horoscopes )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2225, debug=True)
