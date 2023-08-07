import yaml

spidey= {
  "name": "spiderman",
  "powers": [
    "web slinging",
    "spider sense"
  ]
}

with open("spider_data.yml", "w") as fileobj:
    yaml.dump(spidey, fileobj)



with open("spider_data.yml", "r") as yamlfile:
    python_again= yaml.load(yamlfile, Loader=FullLoader)

print(python_again)
