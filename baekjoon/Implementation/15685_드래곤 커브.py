dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

map_data = [[False for _ in range(101)] for _ in range(101)]
        
for _ in range(int(input())):
    c, r, d, g = map(int, input().split())
    map_data[r][c] = True   # 0세대 드래곤 커브 시작점 표시
    
    dir_list = [d]  # 방향 리스트
    # 방향 리스트 만들기
    for _ in range(g):
        for i in range(len(dir_list)-1, -1, -1):
            dir_list.append((dir_list[i]+1) % 4)
    # 드래곤 커브
    for dir in dir_list:
        r += dr[dir]
        c += dc[dir]
        if r < 0 or r > 100 or c < 0 or c > 100:
            continue
        map_data[r][c] = True      
    
# 정사각형 개수 체크
ans = 0
for i in range(100):
    for j in range(100):
        if map_data[i][j] and map_data[i][j+1] and map_data[i+1][j] and map_data[i+1][j+1]:
            ans += 1
print(ans)