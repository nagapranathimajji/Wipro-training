try:
    file=open("File.txt") # Ensure the file name is correct
    # file=open("File1.txt") # Uncomment this line if you want to read from File1.txt.
    str=file.readline()
    strr=file.readline()
    print(str)
    print(strr)
    file.close()
except IOError as e:
    print("File not found or unable to read the file.")
    print(f"Error details: {e}")
else:
    print("File read successfully without any errors.")