n = int(input()) # 홀수
pos = int(input())

map_data = [[0] * n for _ in range(n)]
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
r, c = 0, 0 
d = 0   # 회전 인덱스
map_data[0][0] = n ** 2
for num in range(n**2-1, 0, -1):
    nr = r + dir[d][0]
    nc = c + dir[d][1]
    # 회전
    if nr < 0 or nr >= n or nc < 0 or nc >= n or map_data[nr][nc] != 0:
        d += 1
        d %= 4
        nr = r + dir[d][0]
        nc = c + dir[d][1]
    map_data[nr][nc] = num
    r, c = nr, nc

find_num = []
for i in range(n):
    for j in range(n):
        if map_data[i][j] == pos:
            find_num = [i+1, j+1]
        print(map_data[i][j], end=' ')
    print()
print(*find_num)