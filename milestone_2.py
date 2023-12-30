import random
#Favourite fruits
word_list = ["Apple", "Banana", "Kiwi", "Mango", "Pear"]
#Picks a random fruit from list
word = random.choice(word_list)

print(word)

guess = input("Enter a single letter: ")

#Checks that the length is 1 and is alpahbetical
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
