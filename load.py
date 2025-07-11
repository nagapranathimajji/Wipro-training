import csv
with open('people.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Print each row as a list
        name, age = row
        print(f"Name: {name}, Age: {age}")