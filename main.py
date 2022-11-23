from words import words
import random

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    lives = 6
    word = get_valid_word(words)
    #print("_ "*len(list(word)))
    #print(f"You have {lives} lives")

    letter_word = ser(word)
    letter = input("Choose a letter").upper()
    print(letter)

hangman()