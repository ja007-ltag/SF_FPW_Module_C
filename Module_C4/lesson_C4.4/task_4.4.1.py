def p(n):
    if n == 0:
        return 0
    else:
        print("Begin", n)
        p(n-1)
        print("End", n)


p(10)