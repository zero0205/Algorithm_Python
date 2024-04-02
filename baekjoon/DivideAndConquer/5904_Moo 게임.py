n = int(input())


def dc(k, l, n):    # K, S(K)의 길이, 구하는 순서 N
    if n <= 3:
        return ("m" if n == 1 else "o")
    center = k+3
    left = (l-center)//2
    if n <= left:
        return dc(k-1, left, n)
    elif n > (left+center):
        return dc(k-1, left, n-(left+center))
    else:
        return ("m" if left+1 == n else "o")


# n이 포함된 Moo 수열이 몇번째인지
l = 3
k = 1
while True:
    l = 2*l+k+3
    if l > n:
        break
    k += 1

print(dc(k, l, n))
