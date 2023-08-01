import sqlite3
import requests

conn= sqlite3.connect("astros.db")

url= "http://api.open-notify.org/astros.json"
data= requests.get(url).json()

list_of_astronauts= data["people"]

# uncomment to see this printed out
# print(list_of_astronauts)

conn.execute("""
 CREATE TABLE IF NOT EXISTS ASTROS
 (NAME      TEXT        PRIMARY KEY    NOT NULL,
  CRAFT     TEXT                       NOT NULL);""")

for astro_dict in list_of_astronauts:
    name= astro_dict["name"]
    craft= astro_dict["craft"]

    command= f"INSERT INTO ASTROS (NAME,CRAFT) VALUES ('{name}', '{craft}')"
    conn.execute(command)

conn.commit()

cursor = conn.execute("SELECT * from ASTROS") 
for row in cursor:
    print(row)
