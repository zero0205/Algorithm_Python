import sys
input = sys.stdin.readline
from itertools import product

n = int(input())
board = [0] * (n+1)
total = 0
acc = [[0] * (n+1) for _ in range(n+1)]   # 행별 누적합
for i in range(1, n+1):
    lst = [0] + list(map(int, input().split()))
    board.append(lst)
    for j in range(1, n+1):
        acc[i][j] = acc[i][j-1] + lst[j]
    total += acc[i][n]
    
def divide(x, y, d1, d2):
    section = [0] * 5   # 각 선거구(1~5)별 인구수
    # 각 선거구별 인구수 구하기
    # section 1
    for i in range(1, x):
        section[0] += acc[i][y]
    for i in range(d1):
        section[0] += acc[x+i][y-1-i]
    # section 2
    for i in range(x+1):
        section[1] += (acc[i][n]-acc[i][y])
    for i in range(d2):
        section[1] += (acc[x+1+i][n]-acc[x+1+i][y+1+i])
    # section 3
    for i in range(d2):
        section[2] += acc[x+d1+i][y-d1-1+i]
    for i in range(n-(x+d1+d2-1)):
        section[2] += acc[x+d1+d2+i][y+d2-d1-1]
    # section 4
    for i in range(d1):
        section[3] += (acc[x+d2+1+i][n]-acc[x+d2+1+i][y+d2-1-i])
    for i in range(n-(x+d1+d2)):
        section[3] += (acc[x+d1+d2+1+i][n]-acc[x+d1+d2+1+i][y+d2-d1-1])
    # section 5
    section[4] = total - sum(section[:4])
    return max(section) - min(section)

ans = int(1e9)
for x, y, d1, d2 in product(range(1, n+1), range(1, n+1), range(1, n+1), range(1, n+1)):
    if (y-d1) < 1 or (x+d1+d2) > n or (y+d2) > n:
        continue
    ans = min(ans, divide(x,y,d1,d2))
print(ans)