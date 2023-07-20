# LOOPING OVER
# LIST             element by element
# STRING           character
# DICTIONARY       keys

groceries= ["eggs","milk","lettuce","steak"]
instructor= "chad"
answer= 42
xmen_stats= {"name":"Wolverine",
             "powers":"regeneration",
             "height":"short"}

for x in groceries:
    print("Don't forget the", x)

for x in instructor:
    print("Gimme an " + x.upper() + "!")

for x in xmen_stats:
    print(x)
