m, n = map(int, input().split())
map_data = []
for _ in range(m):
    map_data.append(input())

visited = [[[False] * 4 for _ in range(n)] for _ in range(m)]
cnt = 0
for i in range(1, m-1):
    for j in range(1, n-1):
        for d in [1, -1]:
            # 가로 그림
            if map_data[i][j] == '.' and map_data[i][j+1] == '.':
                if map_data[i+d][j] == 'X' and map_data[i+d][j+1] == 'X' and not visited[i][j][d+1]:
                    visited[i][j][d+1] = True
                    visited[i][j+1][d+1] = True
                    cnt += 1    
            # 세로 그림
            if map_data[i][j] == '.' and map_data[i+1][j] == '.': 
                if map_data[i][j+d] == 'X' and map_data[i+1][j+d] == 'X' and not visited[i][j][d+2]:
                    visited[i][j][d+2] = True
                    visited[i+1][j][d+2] = True
                    cnt += 1
print(cnt)