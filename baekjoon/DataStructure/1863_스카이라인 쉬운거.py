import sys
input = sys.stdin.readline

n = int(input())
skyline = []
for _ in range(n):
    skyline.append(list(map(int, input().split())))

building = []
ans = 0
for i in range(n):
    while building:
        if building[-1] > skyline[i][1]:
            building.pop()
            ans += 1
        elif building[-1] == skyline[i][1]:
            building.pop()
            break
        else:
            break
    building.append(skyline[i][1])

while building:
    a = building.pop()
    if a != 0:
        ans += 1
        
print(ans)