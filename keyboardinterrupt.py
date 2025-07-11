# KeyboardInterrupt Handler
# This code snippet demonstrates how to handle a KeyboardInterrupt exception,
# which occurs when the user interrupts the program execution, typically by pressing Ctrl+C.
try:
    num=int(input("Enter a number: "))
    print(num*4)
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting gracefully.")
except ValueError: 
    print("Invalid input. Please enter a valid number.")
print("Program has ended.")

# This code snippet demonstrates how to handle a KeyboardInterrupt exception, ValueError, using a single try - multiple except blocks.


try:
    num=int(input("Enter a number: "))
    print(num*4)
except (KeyboardInterrupt, ValueError, TypeError):
    print("\nValue has to be entered but Program is interrupted by user. Exiting gracefully.")
print("Program has ended.")