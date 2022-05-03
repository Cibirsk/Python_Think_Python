#Write a function named uses_all that takes a word 
# and a string of required letters,
# and that returns True if the word uses all the required letters at least once. 
# How many words are there that use all the vowels aeiou? How about aeiouy?

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


print(uses_all("papavs", "apsv"))