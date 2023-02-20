
n = int(input())

# 지뢰 위치 입력
bomb = []
for i in range(n):
    arr = input()
    for j in range(n):
        if arr[j] == '*':   # 지뢰 위치 저장
            bomb.append([i, j])
    
# 주변에 몇 개의 지뢰가 있는지
def get_bomb_num(x, y):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    
    res = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if [nx, ny] in bomb:
                res += 1
    return res

# 열린 칸 입력        
board = [[-1] * n for _ in range(n)]
bomb_open = False
for i in range(n):
    row = input()
    for j in range(n):
        # 열린 칸
        if row[j] == 'x':   
            if [i, j] not in bomb:  # 지뢰가 아닌 칸
                board[i][j] = get_bomb_num(i, j)
            else:                   # 지뢰인 칸 -> 지뢰 있는 모든 칸 열어야 함
                if not bomb_open:
                    for bx, by in bomb:
                        board[bx][by] = '*'
                    bomb_open = True
        # 안 열린 칸
        else:               
            if [i, j] not in bomb:  # 지뢰가 아닌칸
                board[i][j] = '.'
            else:                   # 지뢰인 칸
                if bomb_open:
                    continue        # 이미 지뢰 처리 완료
                else:
                    board[i][j] = '.'
                    
for i in range(n):
    for j in range(n):
        print(board[i][j], end='')
    print()