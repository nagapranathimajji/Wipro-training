import csv
# csv module
with open('people.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['name', 'age'])
    for i in range(2):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        # Write the data
        writer.writerow([name, age])

print("Data has been written to people.csv")