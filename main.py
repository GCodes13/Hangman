#Created by GCodes13, special thanks to CodeCademy for the idea! 
#Find GCode on github at github.com/GCodes13
#import neciccary modules:
from random import choice
from time import sleep

dictionary = []
with open("dictionary.txt") as dictionary_words:
  for word in dictionary_words:
    dictionary.append(word)

 hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def select_word():
  return random.choice(dictionary)

def hangman_gameplay(word):
  hangman_stage = 0
  remaining_lives = 6
  guessed_letters = []
  word_list = [letter if letter in guessed_letters else '-' for letter in word]

  while remaining_lives != 0:
    print(hangman_stages[hangman_stage])
    print("\n")
    print(word_list)
    print("\n")
    guess = input("Guess a letter:\n> ")
    if guess in guessed_letters:
      print("You already thought of that letter. Try again with a different letter!")
    elif guess in word:
      print("Good job! The letter {letter} is in the word!".format(letter=guess))
    elif guess not in word:
      print("Sorry, but the letter {letter} is not in the word.".format(letter-guess))
      remaining_lives -= 1
      hangman_stage += 1
    else:
      print("Something went wrong. Please try again.")

print("welcome to Hangman!")
while True:
  hangman_gameplay(select_word())
  while keep_going == True:
    play_again = ("would you like to play again?(y/n)")
    if play_again.lower() == "y":
      print("Okay, let's play again! Loading another game...")
      keep_going == False
    elif play_again.lower() == "n":
      print("That's okay! Come back anytime to play hangman with me!")
      keep_going == False
      exit()
    else:
      print("Sorry, the only available options are 'y' and 'n'. Please pick one of these available options.")
  
  
  
