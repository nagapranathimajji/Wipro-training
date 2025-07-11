import json
name=input("Enter your name: ")
age=int(input("Enter your age: "))

user={"name": name, "age": age}

# now we will create a json file and write to the json file using python

with open("user.json", "w") as file:
    json.dump(user, file)
print("User data has been written to user.json")

with open("user.json", "r") as file:
    loaded = json.load(file)
    print("Data read from user.json:", loaded)