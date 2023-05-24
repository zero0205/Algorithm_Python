import sys 
input = sys.stdin.readline

n = int(input())
town = []   # 마을 위치, 각 마을 인구수
total = 0   # 총 인구수
for i in range(n):
    x, a = map(int, input().split())
    town.append([x, a])
    total += a
    
town.sort()

cnt = 0
for x, a in town:
    cnt += a
    if cnt >= total / 2:
        print(x)
        break