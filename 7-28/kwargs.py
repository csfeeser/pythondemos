def bio(name, age, food, book, movie):
    print(f"{name} is {age} and enjoys a big ol' plate of {food} either reading '{book}' or watching {movie}' on Netflix!")

bio(name="Chad", food="ice cream", book="Ender's Game", movie="Indiana Jones: Last Crusade", age=38)

bio_dict= {"name": "Chad",
           "age": 38,
           "food": "cajun chicken",
           "book": "Captain Blood",
           "movie": "The Shawshank Redemption"}

bio(**bio_dict)
