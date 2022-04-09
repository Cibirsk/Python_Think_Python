def is_triangle():
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))

    if (a > b+c) or (b > a+c) or (c > a+b):
        print("ce n'est pas un triangle")
    else:
        print("c'est un triangle")


is_triangle()
