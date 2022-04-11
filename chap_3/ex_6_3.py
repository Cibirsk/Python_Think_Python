from tkinter import W


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) == 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False


print(is_palindrome('abba'))
