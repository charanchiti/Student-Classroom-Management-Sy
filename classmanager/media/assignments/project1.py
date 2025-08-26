people = {
    "Jos": "Is afraid of dogs",
    "Dav": "Plays the piano",
    "Jame": "Can fly an airplane"
}

print("Here are some fun facts:\n")
for person, fact in people.items():
    print(person + ": " + fact)

people["Jos"] = "Is afraid of heights"

people["Jill"] = "Can hula dance"

print("\nAfter some updates:\n")
for person, fact in people.items():
    print(person + ": " + fact)