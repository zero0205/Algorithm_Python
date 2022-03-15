# https://www.acmicpc.net/problem/11399

# n 입력받기
n = int(input())
# p 배열 입력받기
p = list(map(int, input().split()))

p.sort()

res = 0
for i in range(n):
    res += p[i] * (n-i)
print(res)