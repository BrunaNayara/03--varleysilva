""" 
Init the HangmanGame
"""

from hangman import HangmanGame

WORDLIST_FILENAME = "palavras.txt"
NUMBER_OF_GUESSES = 8

HANGMAN = HangmanGame(file_name=WORDLIST_FILENAME, number_of_guesses=NUMBER_OF_GUESSES)
HANGMAN.start_game()
