# Name: Thomas J. Lee
# Project: Mad Libs MVP

# Requirements:
# - Display story with blanks for input words with correct type (nouns, verbs, ... etc.)
# - Ask user to input words to fill in the blanks.
# - Output the story with the blanks filled in.
# - A test suite to test user input.

# Stretch Requirements:
# Randomize the words of the same type (ie shuffle the 5 nouns)).
# Use a dictionary to generate the words.
# Use a differnet data structure to store words.
# Build with TDD
# Use the system module (for accessing command-line arguments)

# Code Requirements:
# Variable assignment
# Function definitions
# Core data types: strings, integers, floats
# Collection types: lists, tuples, dictionary

noun = []
verb = []

def user_input():
    input = input("type")
    noun.append(input)
    return input

def sentence():

    defaultSentence = "There is a *NOUN1* that needs to be a *VERB1*. A nearby *NOUN2* was upset by this."
    noun1 = input("first noun: ")
    noun2 = input("second noun: ")
    verb1 = input("first verb: ")
    defaultSentence.replace("*NOUN1*", noun1, 1)
    defaultSentence.replace("*NOUN2*", noun2, 1)
    defaultSentence.replace("*VERB1*", verb1, 1)
    print(defaultSentence)

def start():
    initialGreeting1 = "Are you ready to play MadLibs? Let's start!"
    print(initialGreeting1)

    initialGreeting2 = "Here is the sentence!"
    print(initialGreeting2)
    sentence()


def replace():
    for i in range(len(sentence.defaultSentence)):
        if i == "*NOUN*":
            input = input("Enter a noun: ")
            noun.append(input)

        if i == "*VERB*":
            input = input("Enter a verb: ")
            verb.append(input)

# def output():
#     defaultSentence = defaultSentence.replace(/%s/g, noun[0]);

sentence()
