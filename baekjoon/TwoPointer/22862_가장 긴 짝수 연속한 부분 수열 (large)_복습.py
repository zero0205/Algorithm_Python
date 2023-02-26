import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
cnt = 0 # 홀수 개수
ans = 0
while end < n:
    if cnt <= k:    
        if arr[end] % 2 == 1:
            cnt += 1
        end += 1
    else:
        if arr[start] % 2 == 1:
            cnt -= 1
        start += 1
    ans = max(ans, end-start-cnt)

print(ans)