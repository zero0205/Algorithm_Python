import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(r)]

# 누적합 구하기
acc = [[0]*(c+1) for _ in range(r+1)]
for i in range(r):
    for j in range(c):
        acc[i+1][j+1] = acc[i][j+1] + acc[i+1][j] - acc[i][j] + picture[i][j]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    light_sum = (acc[r2][c2] - acc[r1-1][c2] -
                 acc[r2][c1-1] + acc[r1-1][c1-1])//((r2-r1+1)*(c2-c1+1))
    print(light_sum)
