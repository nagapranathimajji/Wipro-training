#write which infinitely prints natural numbers.
#Raise a StopIteration exception after displaying first 20 numbers to execute the program.
def display(n):
    while True:
        try:
            n+=1
            if n==21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n,end=" ")

display(0)