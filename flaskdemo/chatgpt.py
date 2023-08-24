def chinese_zodiac_animal(birth_year):
    """takes incoming birth year and returns animal of chinese zodiac"""
    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    return animals[(birth_year - 4) % 12] 

print(chinese_zodiac_animal(1984))
