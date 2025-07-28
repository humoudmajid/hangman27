# Hangman 🕹️

Hangman is a classic word-guessing game. In this Python implementation, the computer selects a random word from a provided list and the player must guess the word one letter at a time before running out of lives.

## Features

- OOP implementation using Python classes
- Random word selection from a customizable list
- Tracks the player’s remaining lives and guessed letters
- Input validation to prevent repeated and invalid guesses
- Clear win/lose game prompts in the console

## How to Play

1. The computer randomly selects a word from the provided word list.
2. Guess one letter at a time. (Only single alphabetical characters are accepted.)
3. Each incorrect guess reduces your number of lives by one.
4. The game ends when you either guess all the letters or run out of lives.

## Getting Started

### Prerequisites

- Python 3.x (no external libraries required)

### Running the Game

1. **Clone this repository:**
    ```bash
    git clone https://github.com/humoudmajid/hangman27.git
    cd hangman
    ```

2. **Update the word list (optional):**
    You can change the `word_list` in the code to include your favorite words.

3. **Run the game:**
    ```bash
    python hangman.py
    ```

## Example Usage

```python
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

if __name__ == "__main__":
    word_list = ["orange", "apple", "banana", "pear", "mango"]
    play_game(word_list)
