import sys
input = sys.stdin.readline
# n : 집의 개수, c : 공유기의 개수
n, c = map(int, input().split())
# 집 좌표 입력받기
house = []
for _ in range(n):
    house.append(int(input()))
    
house.sort()
    
def add_wifi(start, end, cnt):
    global house, wifi, c
    mid = (start + end) // 2
    if cnt == c or start > end:
        return
    else:
        wifi.append(house[mid])
        
        add_wifi(start, mid - 1, cnt + 1)
        add_wifi(mid + 1, end, cnt + 1)

wifi = []
if c % 2 == 0:  # 짝수
    step = n // c
    for i in range(0, len(house) + 1, step):
        wifi.append(house[i])
else:   # 홀수
    start = 0
    end = len(house) - 1
    wifi.append(house[start])
    wifi.append(house[end])
    cnt = 2
    add_wifi(start, end, cnt)
    
wifi.sort()
min_v = int(1e9)
for i in range(0, len(wifi)-1):
    min_v = min(min_v, wifi[i + 1] - wifi[i])
    
print(min_v)