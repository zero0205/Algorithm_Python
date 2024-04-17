from math import sqrt


def prime(num):  # 소수인지 판별
    if num == 0 or num == 1:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    for i in range(n, 5*int(1e9)):
        if prime(i):
            print(i)
            break
