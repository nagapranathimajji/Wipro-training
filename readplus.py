#file number:4
with open ("file2.txt", "r+") as file:
    content = file.read()  # reads the content of the file
    file.seek(0)  # moves the file pointer to the beginning of the file
    file.write("Modification done here")  # writes to the file
    #here the previous content will be overwritten by the new content
    #Outputs: Modification done here
    # Amazon, Infosys, IBM
    # This is appended data
    file.seek(10)
    file.write("                     here")
    #outputs:
    # Modificati                     heresys, IBM
    #This is appended data
    file.close()