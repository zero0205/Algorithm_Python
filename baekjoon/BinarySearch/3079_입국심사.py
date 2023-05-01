import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time = []
for _ in range(n):
    time.append(int(input()))
    
start, end = min(time), max(time) * m
ans = max(time) * m + 1
while start <= end:
    mid = (start + end) // 2
    tmp = 0     # 가능한 인원수
    for i in range(n):
        tmp += mid // time[i]
    if tmp >= m:    
        end = mid - 1
        ans = mid
    else:
        start = mid + 1
print(ans)