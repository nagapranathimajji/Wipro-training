#random - generate numbers, random choices, and more
#randint - generate random integers
import random
#from random import randint, choice, choices, shuffle, sample
print("random number from 10 to 50:", random.randint(10, 50))
print("Random number from 0 to 1:", random.random())
print("Random number from 1.5 to 5.5:", random.uniform(1.5, 5.5))

#choice - select a random element from a sequence
fruits = ["apple", "banana", "cherry", "date"]
print("Random fruit:", random.choice(fruits))

#choices - select multiple random elements from a sequence
print("Random fruits:", random.choices(fruits))
#shuffle - shuffle a sequence in place
random.shuffle(fruits)
print("Shuffled fruits:", fruits)

#seed - set the seed for reproducibility
random.seed(42)
print("Random number with seed 42:", random.randint(10, 50))
#no matter how many times you run this, it will always give the same result
