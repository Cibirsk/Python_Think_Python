def check_fermat():
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    n = int(input('n = '))

    if (a**n) + (b**n) == (c**n):
        print('Fermat was wrong')
    else:
        print('he was right')


check_fermat()

# a = 3
# b = 4
# n = 2
# print(a**n)
