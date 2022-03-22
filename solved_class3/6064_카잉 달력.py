# https://www.acmicpc.net/problem/6064

# # 유클리드 호제법 -> 최대공약수 구하기
# def GCD(x, y):
#     while(y):
#         x, y = y, x % y
#     return y

# # 최대공약수
# def LCM(x, y):
#     if GCD(x, y) != 0:
#         return x * y // GCD(x, y)
#     else:
#         return x * y

# t = int(input())

# for _ in range(t):
#     m, n, x, y = map(int, input().split())
#     last_year = LCM(m, n)
#     find = False
#     for i in range(1, last_year + 1):
#         if i % m == x and i % n == y:
#             print(i)
#             find = True
#             break
#     if find:
#         continue
#     else:
#         print(-1)

# 시간 초과
###############
t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    find = False
    while x <= m * n:
        if (x - y) % n == 0:
            print(x)
            find = True
            break
        x += m
    if find:
        continue
    else:
        print(-1)