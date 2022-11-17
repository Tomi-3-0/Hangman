import random
from data import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()



def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    #getting user inputs
    while len(word_letters) > 0 and lives > 0:
        #letters already used 
        print('You have', lives, 'left and have already used:', " ".join(used_letters))

        #show current word and dashes for letters not yet guessed
        word_List = [letter if letter in used_letters else '_' for letter in word]
        print("Word is: ", " ".join(word_List))


        tried_letters = input('Guess a word: ').upper()
        if tried_letters in alphabet - used_letters:
            used_letters.add(tried_letters)
            if tried_letters in word_letters:
                word_letters.remove(tried_letters)

            else: 
                lives = lives - 1
                print("Letter is not in word") 

        elif tried_letters in used_letters:
            print("Letter has been already used")
        
        else:
            print ("Type a valid character")

    if lives == 0:
        print("Out of lives, the word was", word)
    else: 
        print('You guessed the word', word, '!')

hangman()
# user_input = input('Type something')
# print(user_input)