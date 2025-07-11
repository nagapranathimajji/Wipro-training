import sys
#sys.argv is a list in Python, which contains the command-line arguments passed to the script.
#argv stands for argument variable
if len(sys.argv) < 2:
    print("Usage: python hi.py <name>")
else:
    name=sys.argv[1]
    print(f"Student, {name}!")

# Example usage:
# Save this script as systemarguments.py and run it from the command line:
# python systemarguments.py pranathi
# Output: Student, pranathi!                              
#(base) apple@Apples-MacBook-Pro Wipro training % python systemarguments.py pranathi