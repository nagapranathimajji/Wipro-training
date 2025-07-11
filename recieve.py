# file number:3
with open('binaryfile.bin', 'rb') as file:
    data = file.read()  # reads binary data from the file
    print(data)  # prints the binary data read from the file
    # Outputs: b'this is a sample binary data\n'
    # if the file does not exist, it will raise a FileNotFoundError