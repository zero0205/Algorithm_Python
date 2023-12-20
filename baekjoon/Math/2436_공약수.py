def euclid(a, b):
    if a > b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


a, b = map(int, input().split())
tmp = b//a
for i in range(int(tmp**(1/2)), 0, -1):
    if tmp % i == 0:
        j = tmp // i
        if euclid(i, j) == 1:
            print(i*a, j*a)
            break
