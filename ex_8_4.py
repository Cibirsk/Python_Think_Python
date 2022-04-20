from unittest import result


def test(s):
    for letter in s:
        print(letter + ' : ' + str(ord(letter)))


def test2():
    print('UPPERCASE')
    for i in range(65, 91):  # uppercase 65-90
        print(str(i) + ' : ' + chr(i))

    print('lowercase')
    for i in range(97, 123):  # lowercase 97-122
        print(str(i) + ' : ' + chr(i))


def rotate(s, index):
    result = ''
    for letter in s:
        temp_result = ord(letter)+index

        if letter.isupper():
            if temp_result > 90:
                temp_result = 64 + (temp_result - 90)
            if temp_result < 65:
                temp_result = 91 - (65 - temp_result)

        if letter.islower():
            if temp_result > 122:
                temp_result = 96 + (temp_result - 122)
            if temp_result < 97:
                temp_result = 123 - (97 - temp_result)

        result += chr(temp_result)
    print(result)


rotate('IBM', -1)
