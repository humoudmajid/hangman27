import random

while True:
    guess = input("Guess a letter: ")

    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")


word_list = ["Apple", "Banana", "Kiwi", "Mango", "Pear"]
word = random.choice(word_list)

while True:
    guess = input("Guess a letter: ")

    if len(guess) == 1 and guess.isalpha():
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Testing the code
ask_for_input()
