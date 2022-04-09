def cursive(n, s):
    if n == 0:
        print(s)
    else:
        cursive(n-1, n+s)


cursive(3, 0)
