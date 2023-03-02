board = []
for _ in range(19):
    board.append(list(map(int, input().split())))
    
def check(r, c):
    color = board[r][c]
    
    # 가로
    if c-1 < 0 or board[r][c-1] != color: # 이미 체크한 오목이 아니어야 함
        flag = True
        for i in range(1, 5):
            if c+i >= 19 or board[r][c+i] != color:
                flag = False
                break
        if flag:
            if c+5 >= 19 or board[r][c+5] != color: # 다섯알만 연속
                return True
    # 세로
    if r-1 < 0 or board[r-1][c] != color: # 이미 체크한 오목이 아니어야 함
        flag = True
        for i in range(1, 5):
            if r+i >= 19 or board[r+i][c] != color:
                flag = False
                break
        if flag:
            if r+5 >= 19 or board[r+5][c] != color: # 다섯알만 연속
                return True
    # 대각선 1
    if r-1 < 0 or c-1 < 0 or board[r-1][c-1] != color:  # 이미 체크한 오목이 아니어야 함
        flag = True
        for i in range(1, 5):
            if r+i >= 19 or c+i >= 19 or board[r+i][c+i] != color:
                flag = False
                break
        if flag:
            if r+5 >= 19 or c+5 >= 19 or board[r+5][c+5] != color: # 다섯알만 연속
                return True
    # 대각선 2
    if r+1 >= 19 or c-1 < 0 or board[r+1][c-1] != color:  # 이미 체크한 오목이 아니어야 함
        flag = True
        for i in range(1, 5):
            if r-i < 0 or c+i >= 19 or board[r-i][c+i] != color:
                flag = False
                break
        if flag:
            if r-5 < 0 or c+5 >= 19 or board[r-5][c+5] != color: # 다섯알만 연속
                return True
    return False    # 다섯알 연속 되는게 없음

for i in range(19):
    for j in range(19):
        if board[i][j] > 0:
            if check(i, j):
                print(board[i][j])
                print(i+1, j+1)
                exit()
print(0)