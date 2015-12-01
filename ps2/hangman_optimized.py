import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def choose_word(wordlist):
    """
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# global wordList
wordlist = load_words()


def hangman():
    hidden_word = choose_word(wordlist).lower()
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is {length} letters long".format(length=len(hidden_word))
    incorrect_guesses = 8
    used_letters = {}
    while incorrect_guesses > 0 and not found_hidden_word(hidden_word, used_letters):
        print ">>>>>>>>>>>>>>>>>>>>"
        print "You have {incorrect_guesses} guesses left".format(incorrect_guesses=incorrect_guesses)
        print "Available Letters: " + get_available_letters(used_letters)
        new_letter = request_letter(used_letters)
        if new_letter in hidden_word:
            print "Good guess: " + get_hidden_word(hidden_word, used_letters)
        else:
            print "Oops! That letter is not in my word " \
                  + get_hidden_word(hidden_word, used_letters)
            incorrect_guesses -= 1
            if incorrect_guesses == 0:
                print "Sorry, you ran out of guesses. The word was " \
                      + hidden_word + ". Play again!"
                break
        print
        if found_hidden_word(hidden_word, used_letters):
            print "Congratulations, you won!"


def get_hidden_word(hidden_word, used_letters):
    """Returns a string of the form __ad___ by filling in correct guesses"""
    visible_word = ""
    for letter in hidden_word:
        if letter in used_letters:
            visible_word += letter
        else:
            if len(visible_word) > 0 and visible_word[-1] == '_':
                visible_word += " "
            visible_word += "_"
    return visible_word


def found_hidden_word(hidden_word, used_letters):
    """Returns True if the word has been completely uncovered"""
    for letter in hidden_word:
        if letter not in used_letters:
            return False
    return True


def get_available_letters(used_letters):
    """Returns a list of lowercase letters not in used_letters"""
    available_letters = ""
    for letter in string.lowercase:
        if letter not in used_letters:
            available_letters += letter
    return available_letters


def request_letter(used_letters):
    """Asks for another guess and returns (gameover, victory) """
    new_letter = raw_input("Please guess a letter: ").lower()
    used_letters[new_letter] = 1
    return new_letter

hangman()
