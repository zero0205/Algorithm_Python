# https://www.acmicpc.net/problem/1780

import sys
input = sys.stdin.readline

n = int(input())

paper = []
ans = [0, 0, 0]

for _ in range(n):
    paper.append(list(map(int, input().split())))

def cutting(x, y, map_data, n):
    global ans
    num = map_data[x][y]
    for i in range(n):
        if n == 1:
            break
        for j in range(n):
            if num != map_data[x + i][y + j]:
                cutting(x, y, map_data, n // 3)
                cutting(x, y + n //3, map_data, n // 3)
                cutting(x, y + (n // 3) * 2, map_data, n // 3)
                
                cutting(x + n //3, y, map_data, n // 3)
                cutting(x + n //3, y + n //3, map_data, n // 3)
                cutting(x + n //3, y + (n // 3) * 2, map_data, n // 3)
                
                cutting(x + (n // 3) * 2, y, map_data, n // 3)
                cutting(x + (n // 3) * 2, y + n //3, map_data, n // 3)
                cutting(x + (n // 3) * 2, y + (n // 3) * 2, map_data, n // 3)
                return
    if num == -1:
        ans[0] += 1
    elif num == 0:
        ans[1] += 1
    else:
        ans[2] += 1
    return

cutting(0,0,paper,n)
for a in ans:
    print(a)