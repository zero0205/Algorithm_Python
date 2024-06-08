import sys
input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input())
map_data = [input() for _ in range(m)]

# 누적합
accum = [[[0]*3 for _ in range(n+1)] for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        accum[i][j][0] = accum[i-1][j][0]+accum[i][j-1][0]-accum[i-1][j-1][0]
        accum[i][j][1] = accum[i-1][j][1]+accum[i][j-1][1]-accum[i-1][j-1][1]
        accum[i][j][2] = accum[i-1][j][2]+accum[i][j-1][2]-accum[i-1][j-1][2]
        if map_data[i-1][j-1] == 'J':
            accum[i][j][0] += 1
        elif map_data[i-1][j-1] == 'O':
            accum[i][j][1] += 1
        else:
            accum[i][j][2] += 1

for _ in range(k):
    ltx, lty, rbx, rby = map(int, input().split())
    j = accum[rbx][rby][0]-accum[ltx-1][rby][0] - \
        accum[rbx][lty-1][0]+accum[ltx-1][lty-1][0]
    o = accum[rbx][rby][1]-accum[ltx-1][rby][1] - \
        accum[rbx][lty-1][1]+accum[ltx-1][lty-1][1]
    i = accum[rbx][rby][2]-accum[ltx-1][rby][2] - \
        accum[rbx][lty-1][2]+accum[ltx-1][lty-1][2]
    print(j, o, i)
