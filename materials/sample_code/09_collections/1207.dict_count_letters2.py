alphabets = "abcdefghijklmnopqrstuvwxyz"

stringA = input("Please enter a string: ")
stringA = stringA.lower()

dict = {}

for letter in stringA:
    # alphabets = alphabets + alphabets[letter]
    alphabets.update(letter, )