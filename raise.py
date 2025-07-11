# Raise Exception
# Raise an exception using the raise statement

'''try:
    num=11
    print(num)
    raise ValueError
except:
    print("Exception occured.")'''

# traceback most recent calls

try:
    print("Raising Exception")
    raise ValueError
except:
    print("Exception caught ....")
finally:
    print("performing clean-up in finally")

#finally block executes regardless of the above code



#assertion - used to check conditions
# This code uses an assertion to check if the temperature in Fahrenheit is less than or equal to 32.
# If the condition is not met, it raises an AssertionError with the message "Its cold

c = int(input("Enter temperature in c: "))
f = (c * 9/5) + 32
assert(f<=32),"Its cold"
print(f"Temperature in Fahrenheit: {f}")
