#write a program to create a text file, access the text file data and use the data to 
#split the lines into series of words and use space to perform split operation
#sample.txt:
#Hello students
#How are you today
#output:
#['Hello', 'students','How', 'are', 'you', 'today']

file=open("sample.txt", "w")  # opens the file in write mode
file.write("Hello students\nHow are you today")  # writes to the file
file.close()  # closes the file

print("File created and data written successfully.")

file = open("sample.txt", "r")  # opens the file in read mode
data = file.read()  # reads the content of the file
file.close()  # closes the file

print("data is accessed successfully.")
words = data.split()  # splits the data into words using space as the delimiter
print("Words in the file:", words)  # prints the list of words