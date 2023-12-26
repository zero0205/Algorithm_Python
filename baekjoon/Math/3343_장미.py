from math import ceil
import sys
input = sys.stdin.readline

n, a, b, c, d = map(int, input().split())

if b/a < d/c:   # cd의 가성비가 더 안 좋다면 ab와 cd 바꾸기
    a, b, c, d = c, d, a, b

ans = sys.maxsize
for i in range(c):  # ab 개수
    c_num = ceil((n-i*a)/c)
    if c_num < 0:
        c_num = 0
    ans = min(ans, i*b+c_num*d)
    if c_num == 0:
        break
print(ans)
