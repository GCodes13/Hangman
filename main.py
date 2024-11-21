## Created by GCodes13, special thanks to CodeCademy for the idea! 
# Find GCode on github at github.com/GCodes13
# Import necessary modules:
from random import choice
from time import sleep

# Load dictionary
dictionary = ["avacado","hello"]
hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def select_word():
    return choice(dictionary)  # Use choice instead of random.choice

def hangman_gameplay(word):
    hangman_stage = 0
    remaining_lives = 6
    guessed_letters = []
    word_list = ['-' for _ in word]  # Initialize with '-' for each letter

    while remaining_lives != 0 and '-' in word_list:
        print(hangman_stages[hangman_stage])
        print("\n")
        print("Current word: " + ''.join(word_list))  # Join list to display as a string
        print("\n")
        guess = input("Guess a letter:\n> ").lower()  # Convert guess to lowercase
        if guess in guessed_letters:
            print("You already thought of that letter. Try again with a different letter!")
        else:
            guessed_letters.append(guess)  # Add guessed letter to the list
            if guess in word:
                print("Good job! The letter {letter} is in the word!".format(letter=guess))
                # Update word_list with the guessed letter
                for index, letter in enumerate(word):
                    if letter == guess:
                        word_list[index] = letter
            else:
                print("Sorry, but the letter {letter} is not in the word.".format(letter=guess))
                remaining_lives -= 1
                hangman_stage += 1

    if '-' not in word_list:
        print("Congratulations! You've guessed the word: " + word)
    else:
        print("Game over! The word was: " + word)

print("Welcome to Hangman!")
keep_going = True  # Initialize keep_going
while True:
    hangman_gameplay(select_word())
    while keep_going:
        play_again = input("Would you like to play again? (y/n)").lower()
        if play_again == "y":
            print("Okay, let's play again! Loading another game...")
            keep_going = False
        elif play_again == "n":
            print("That's okay! Come back anytime to play hangman with me!")
            exit()
        else:
            print("Sorry, the only available options are 'y' and 'n'. Please pick one of these available options.")
    keep_going = True  # Reset for the next game
