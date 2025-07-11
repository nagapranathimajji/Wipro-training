#file number:6
with open("file2.txt", "r") as file:
    lines=file.readlines()  # reads all lines from the file
print("list of lines:",lines)
#outputs:
# list of lines: ['Modificati                     heresys, IBM\n', 'This is appended dataThis is Appended data\n', '\n']

for line in lines:
    print(line.strip())  # prints each line without leading/trailing whitespace
#outputs:
# Modificati                     heresys, IBM
# This is appended dataThis is Appended data

with open("file2.txt", "r") as file:
    separate_line=[line.strip() for line in file.readlines()]  # reads all lines from the file and removes leading/trailing whitespace
print("separate line:", separate_line)


#here we used list comprehension to read all lines from the file and remove leading/trailing whitespace
#outputs:
# separate line: ['Modificati                     heresys, IBM', 'This is appended dataThis is Appended data']


file=open("file2.txt", "r")  # opens the file in read and write mode
print(file.closed)
file.close()  # closes the file manually
print(file.closed)  # checks if the file is closed