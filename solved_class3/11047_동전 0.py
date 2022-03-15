# https://www.acmicpc.net/problem/11047

# n, k 입력받기
n, k = map(int, input().split())
# 동전의 가치 입력받기
a = []
for _ in range(n):
    a.append(int(input()))

# 내림차순으로 정렬    
a.sort(reverse=True)

# 그리디
ans = 0
for coin in a:
    if k == 0:
        break
    else:
        num = k // coin
        k -= num * coin
        ans += num

print(ans)