import itertools
data = input("Enter a string/characters: ")
permute=list(itertools.permutations(data))
print("Permutations of the given string/characters:")
for i in permute:
    print(' '.join(i))
print("Total permutations:", len(permute))