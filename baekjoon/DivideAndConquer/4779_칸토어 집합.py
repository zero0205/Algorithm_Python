def dc(n):
    if n == 0:
        print('-', end="")
        return
    dc(n-1)
    print(' '*(3**(n-1)), end="")
    dc(n-1)


while True:
    try:
        dc(int(input()))
        print()
    except EOFError:
        break
