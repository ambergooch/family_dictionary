my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    },
    "brother": {
        "name": "Charlie",
        "age": 32
    }
}

for key in my_family.keys():
    print(f"{my_family[key]['name']} is my {key} and is {my_family[key]['age']} years old")

for fam_member, details in my_family.items():
    print(f"{details['name']} is my {fam_member} and is {details['age']} years old")

family = {value["name"] + " is my " + key + " and is " + str(value["age"]) + " years old" for (key, value) in my_family.items()}

for person in family:
    print(person)