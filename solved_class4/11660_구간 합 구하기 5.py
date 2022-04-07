# https://www.acmicpc.net/problem/11660

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 누적합 구해놓기
for i in range(1, n):
    data[0][i] += data[0][i-1]
    data[i][0] += data[i-1][0]
    
for i in range(1, n):
    for j in range(1, n):
        data[i][j] += data[i-1][j] + data[i][j-1] - data[i-1][j-1]
    
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1:
        print(data[x2-1][y2-1])
    elif x1 == 1:
        print(data[x2-1][y2-1] - data[x1-1][y1-2])
    elif y1 == 1:
        print(data[x2-1][y2-1] - data[x1-2][y1-1])
    else:
        print(data[x2-1][y2-1] - (data[x1-2][y2-1] + data[x2-1][y1-2] - data[x1-2][y1-2]))