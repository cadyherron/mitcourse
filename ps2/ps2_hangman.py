import random
import string

WORDLIST_FILENAME = "words.txt"
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
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
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def partial_word(word_to_guess, guessed_letters):
    result = ''
    for letter in word_to_guess:
        if letter in guessed_letters:
            result = result + letter
        else:
            result += '_ '
    return result


def hangman_game(wordList, num_guesses=5):
    alphabet = ALPHABET
    guessed_letters = []

    # computer chooses a word
    word_to_guess = choose_word(wordList)
    num_letters = len(word_to_guess)
    print ("Welcome to the game, Hangman!\n"
           "I am thinking of a word that is {num_letters} letters long.".format(num_letters=num_letters))

    while num_guesses >= 0:
        print "You have {number} guesses left.".format(number=num_guesses)
        print "Available letters: ", ''.join(alphabet)
        guess = raw_input('Please guess a letter: ').lower()
        print "----------------------"
        if guess in guessed_letters:
            print "You already guessed that letter, silly! Please guess again."
        elif guess not in ALPHABET:
            print "That's not a letter. Please guess again."
        else:
            guessed_letters.append(guess)
            alphabet.remove(guess)
            partial = partial_word(word_to_guess, guessed_letters)
            if guess in word_to_guess:
                if partial == word_to_guess:
                    print "Congratulations, you won! The word is: ", word_to_guess
                else:
                    print "Good guess: ", partial
            else:  # letter is not in the word
                if num_guesses == 1:  # player just used their last guess
                    print "Sorry, you lost! The word was: ", word_to_guess
                    break
                else:
                    print "Oops! That letter is not in my word:", partial
                    num_guesses -= 1


hangman_game(wordList=load_words())