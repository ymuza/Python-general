"""Assignment: Anagram Checker
Objective: The goal of this assignment is to assess your problem-solving skills and your
ability to explain a technical concept or express it in a structured, logical manner using pseudo-code.
The Challenge: Anagram Checker
An anagram is a word or phrase formed by rearranging the letters of another word or phrase
, using all the original letters exactly once. For example, "cinema" is an anagram of "iceman".
Your Task:
Write a function that checks if two given words are"""


"""Roma
AMOR
Listen
SIlent"""


def anagram_checker(word1, word2):
    # normalize both words to lowecase
    word2 = word2.lower()
    word1 = word1.lower()

    char_list1 = []

    # if both words have the same amount of letters, we can continue
    if len(word1) == len(word2): #

        for i in word2: #go through each letter in word2
           if i in word1: # see if each letter is in word1
             char_list1.append(i) #adds the letter to a list
           else:
               return "not an anagram" # if letter is not in the word, its not an anagram

        if len(char_list1) == len(word1): # compares the length of the list and the word1 variable. same length => anagram
            print("anagram")


anagram_checker("amor", "roma")