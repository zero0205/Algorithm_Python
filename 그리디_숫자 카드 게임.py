# 그리디
# 2. 숫자 카드 게임

n, m = map(int, input().split())

lst = [0 for i in range(n)]

for i in range(n):
    lst[i] = list(map(int, input().split()))

ans = -1

for i in lst:
  if min(i) > ans:
    ans = min(i)

print(ans)