def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False


def is_palindrome2(word):
    if word == word[::-1]:
        return True
    return False


print(is_palindrome2('rbcdcba'))
