import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()

start, end = 1, house[-1] - house[0]
ans = 0
while start <= end:
    mid = (start + end) // 2
    now = house[0]
    num = 1
    
    for i in range(1, len(house)):
        if house[i] >= now + mid:
            now = house[i]
            num += 1
        
    if num >= c:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(ans)