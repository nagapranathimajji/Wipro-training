from collections import Counter
# Function to count the frequency of each character in a string
text = input("Enter a string: ")
char_count = Counter(text)
# Display the character frequencies
print("Character frequencies:", dict(char_count))