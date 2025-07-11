#file number: 1
#needs file2.txt



# fileobj=(filename[,access_mode])
#access modes:
# 'r' - read (default) which opens a file for reading only
# if you give a non-existent file name, it will raise an error
# 'rb' - read binary which opens a file for reading in binary mode
# 'r+' - read and write which opens a file for both reading and writing
# 'rb+' - read and write binary which opens a file for both reading and writing in binary mode
# 'w' - write which opens a file for writing only, truncating the file first.
# when you give a non-existent file name, it will create a new file and if the file exists, it will truncate the file
# then the old content will be lost and rewritten by new content.
# 'wb' - write binary which opens a file for writing in binary mode, truncating the file first.
# 'w+' - write and read which opens a file for both writing and reading, truncating the file first.
# 'wb+' - write and read binary which opens a file for both writing and reading in binary mode, truncating the file first.
# 'a' - append which opens a file for appending, which means that the file pointer is at the end of the file
# when you give a non-existent file name, it will create a new file and if the file exists, it will not truncate the file


#fileobj attributes
# fileobj.name - returns the name of the file
# fileobj.mode - returns the access mode of the file
# fileobj.closed - returns True if the file is closed, False otherwise
# fileobj.readable() - returns True if the file is readable, False otherwise
# fileobj.writable() - returns True if the file is writable, False otherwise

'''file=open("file2.txt", "r")
print(file.name)  # prints the name of the file
print(file)'''

with open("file2.txt", "r") as file:
    content= file.read()
    print(content)  # prints the content of the file
    file.close()  # closes the file
    #Outputs: Hello Students!!!!!!

with open("file2.txt", "w") as file:
    file.write("Wipro, TCS, Capgemini")  # writes to the file
    file.close()  # closes the file
    #Outputs: Wipro, TCS, Capgemini

with open("file2.txt", "w") as file:
    file.write("Google, Microsoft, cat\n")  # appends to the file
    file.write("Amazon, Infosys, IBM\n")  # appends to the file
    file.close()  # closes the file
    #Outputs: Google, Microsoft, cat
    #Amazon, Infosys, IBM


with open("file2.txt", "a") as file:
    file.write("This is appended data")  # appends to the file
    file.close()  # closes the file
    #Outputs: Google, Microsoft, cat
    #Amazon, Infosys, IBM
    #This is appended data