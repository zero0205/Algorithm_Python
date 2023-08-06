s, n, k, r1, r2, c1, c2 = map(int, input().split())

if s == 0:
    print(0)
    exit()

# (x, y)가 검은색인지 흰색인지 판단
def fractal(length, x, y):
    if length == 1:
        return 0
    c = length//n   # n개로 나눠졌을때 길이
    # 검은 부분에 해당되면 1 리턴
    if (c * (n-k)//2) <= x < (c * (n+k)//2) and (c * (n-k)//2) <= y < (c * (n+k)//2):
        return 1
    return fractal(c, x%c, y%c)

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(fractal(n**s, i, j), end='')
    print()