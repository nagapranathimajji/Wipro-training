# file number:2

data=b'this is a sample binary data\n'
with open("binaryfile.bin", "wb") as file:
    file.write(data)  # writes binary data to the file
    file.close()  # closes the file
    # Outputs: this is a sample binary data
    #as this file is non-existent, it will create a new file and write the data to it.