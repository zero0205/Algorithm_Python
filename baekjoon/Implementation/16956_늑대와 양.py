r, c = map(int, input().split())
map_data = []
for i in range(r):
    map_data.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(r):
    for j in range(c):
        if map_data[i][j] == 'W':
            for d in range(4):
                nx = i+dx[d]
                ny = j+dy[d]
                if 0 <= nx < r and 0 <= ny < c:
                    if map_data[nx][ny] == 'S':
                        print(0)
                        exit()
                    if map_data[nx][ny] == '.':
                        map_data[nx][ny] = 'D'
print(1)
for i in range(r):
    print(*map_data[i], sep='')
