def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def count(word, letter, start):
    count = 0
    word = word[start:]
    for i in word:
        if i == letter:
            count = count + 1
    return count


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)-1
    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True


# s = 'mike and bob'
# print(s.replace('i', 'A'))

# a = "MIKE,,-_"
# b = a.strip(",;:_- ")
# print(b)

# c = "abcda"
# print(c.count("a"))

# fruit = 'banana'
# print(fruit[::2])
jack_age = 23
alex_age = 2 
lana_age = 1 

if jack_age < alex_age and jack_age < lana_age:
    print(jack_age)
elif alex_age < jack_age and alex_age < lana_age:
    print(alex_age)
else:
    print(lana_age)
