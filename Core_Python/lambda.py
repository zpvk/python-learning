people = [
    {"name": "Harry", "House":"Minimuthu"},
    {"name": "Cho","House":"Slytherin"},
    {"name":"Draco", "house":"Slytherin"}
]

people.sort(key=lambda perosn: perosn["name"])
print(people)
