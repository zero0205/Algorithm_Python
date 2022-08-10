import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

acc = [0]
# 누적합 구하기
for i in range(1, n + 1):
    acc.append(acc[i-1] + arr[i-1])

start, end = 0, 0
ans = 100001
while start < n: 
    if acc[end] - acc[start] < s:
        if end == n:
            break
        end += 1
    else:
        ans = min(ans, end - start)
        start += 1

if ans == 100001:        
    print(0)
else:
    print(ans)
    