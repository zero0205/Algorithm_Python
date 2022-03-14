# https://www.acmicpc.net/problem/2630

from collections import deque

n = int(input())
# 색종이 입력
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))
white = 0
blue = 0
# 모두 같은 색으로 칠해져있는지 확인하는 함수
def check(x, y, n):
    global white, blue
    
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                check(x, y, n // 2)
                check(x, y + n // 2, n // 2)
                check(x + n // 2, y, n // 2)
                check(x + n // 2 , y + n // 2, n // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1
        
check(0, 0, n)
print(white)
print(blue)