#file number: 5
with open("file2.txt", "a+") as file:
    file.write("Appended data\n")  # appends to the file
    file.seek(0)  # moves the file pointer to the beginning of the file
    print(file.read())  # reads the content of the file
    file.close()  # closes the file
    # Outputs: Modificati                     heresys, IBM
    #This is appended dataAppended data