# file methods
# fileno() - file number in your tool
# flush()- clears the write buffer from input
# isatty() - returns boolean type output, file stream is interactive or not
# readline(n) - particular line
# truncate(n)- reallocates the file size byte
# rstrip() - removes trailing whitespace from the end of the string
# seek(n) - moves the file pointer to the nth byte
# tell() - returns the current position of the file pointer
# write(string) - writes a string to the file

with open("file2.txt", "r") as file1, open("file3.txt", "r") as file2:
    content1 = file1.read()  # reads the content of the file
    content2 = file2.read()  # reads the content of the file
    print("Content of file1:", content1)  # prints the content of the first file
    print("Content of file2:", content2)  # prints the content of the second
    file1.close()  # closes the first file
    file2.close()  # closes the second file