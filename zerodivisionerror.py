#Exception Handling
# types of errors syntax, logical...
# built-in exceptions
# 1. Exceptionn - base class for all exception
# 2. StopIteration - next() method does'nt point to any object
# 3. SystemExit - sys.exit() function will raise
# 4. StandardError 
# 5. ArithmeticError - math cal /10
# 6. OverflowError - numeric type exceeding the limit of its size
# 7. ZeroDivisionError 10/0
# 8. AssertionError - Assert statement
# 9. EOFError - till ennd of last statement, when no IO or return value occurs
# 10. ImportError
# 11. KeyboardInterrupt
# 12. LookupError
# 13. IndexError - performs under dict,list,tuple,set
# 14. NameError - variable not defined
# 15. EnvironmentError - IO related errors
# 16. IOError - IO related errors
# 17. SystemError - internal error in python interpreter
# 18. ValueError - function receives argument of correct type but inappropriate value
# 19. TypeError - operation not supported for the type of object
# 20. RuntimeError - error that does not fall under any of the above categories
# 21. SyntaxError - error in syntax
# 22. IndentationError - error in indentation
# 23. TabError - mixing tabs and spaces in indentation
# 24. MemoryError - memory allocation error
# 25. NotImplementedError - method or function not implemented

num=int(input("Enter a numerator: "))
deno=int(input("Enter a denominator: "))
try:
    result = num / deno
    print(f"The result of {num} divided by {deno} is {result}.")
except ZeroDivisionError:   # specific exception handling
    print("Error: Division by zero is not allowed.")    