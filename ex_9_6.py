# Write a function called is_abecedarian that returns True 
# if the letters in a word
# appear in alphabetical order (double letters are ok). 
# How many abecedarian words are there?

def is_abcd(word):
    i = 0
    while i < (len(word) - 1):
        if word[i+1] < word[i]:
            return False
        i +=1
    return True

print(is_abcd("abedd"))