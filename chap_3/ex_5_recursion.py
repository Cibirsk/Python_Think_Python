def blast(s, n):
    if n <= 0:
        return
    print(s + str(n))
    blast(s, n-1)


blast('top ', 5)
