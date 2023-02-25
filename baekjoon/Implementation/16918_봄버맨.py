r,c,n = map(int, input().split())
map_data = []
for _ in range(r):
    map_data.append([[bomb, 0] for bomb in list(input())])

def explosion(x, y):
    map_data[x][y][0] = '.'
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if map_data[nx][ny][1] < 2:     # [nx][ny]가 이번에 터지는 폭탄이 아니면
                map_data[nx][ny] = ['.', -1]
            
sec = 0
while sec < n:
    sec += 1
    for i in range(r):
        for j in range(c):
            if map_data[i][j][0] == 'O':
                map_data[i][j][1] += 1
                if map_data[i][j][1] >= 3:  # 이번에 터지는 폭탄
                    explosion(i, j)
            else:
                if sec % 2 == 0 and sec > 1:    
                    map_data[i][j] = ['O', 0]   # 폭탄 설치

for i in range(r):
    for j in range(c):
        print(map_data[i][j][0], end='')
    print()