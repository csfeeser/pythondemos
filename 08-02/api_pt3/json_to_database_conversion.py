import sqlite3
import json

# GOAL: convert the contents of "marvel_data" into the content of a database

# open the old file with JSON data
with open("marvel_data.json") as data:
     data= json.load(data)

# connect to a db file
conn = sqlite3.connect('marvel.db')

# build a table named MARVEL
conn.execute('''CREATE TABLE IF NOT EXISTS MARVEL
 (NAME        TEXT                    NOT NULL,
  ALTEREGO    TEXT                    NOT NULL,
  ABILITIES   JSON,
  AGE         INT);''')

# loop over all the hero dictionaries:
# save each hero's info in a separate value
for char in data:
    name= char["hero_name"]
    alterego= char["alter_ego"]
    abilities= char["abilities"]
    abilities= json.dumps(abilities) # <-- convert into a double quoted string so we can put it in the table
    age= char["age"]

    command = f"INSERT INTO MARVEL (NAME, ALTEREGO, ABILITIES, AGE) VALUES ('{name}', '{alterego}', '{abilities}', {age})"
    
    # print each command for debugging purposes (ensures its written the way we want)
    print(command)
    conn.execute(command)

# always close a connection when you are done with it!
conn.commit()
conn.close()
