# rather than look at ALL the code in the old script,
# we'll tinker out a solution in a separate file.




# GOAL: edit the code below so we return a list of dictionaries from the database

with open("marvel_data.json") as data:
    marvel_characters= json.load(data)

def characterlist(hero_choice):
    """takes a hero name, returns a list of characters who match"""
    matches= []
    for char in marvel_characters:
        if char["hero_name"].lower() == hero_choice.lower():
            matches.append(char)
    return matches


# hard-coding in a search for Thor
characterlist("thor")
