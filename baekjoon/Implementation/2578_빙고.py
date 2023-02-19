board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
                 
def bingo():
    res = 0
    # 가로, 세로 확인
    for i in range(5):
        row_cnt = 0
        col_cnt = 0
        for j in range(5):
            if board[i][j] == 0:    # 가로 확인
                row_cnt += 1
            if board[j][i] == 0:    # 세로 확인
                col_cnt += 1
        if row_cnt == 5:
            res += 1
        if col_cnt == 5:
            res += 1
    # 대각선 확인
    diagnol1 = 0
    diagnol2 = 0
    for i in range(5):
        if board[i][i] == 0:    # 왼위->오른아래
            diagnol1 += 1
        if board[i][4-i] == 0:  # 오른위->왼아래
            diagnol2 += 1
    if diagnol1 == 5:
        res += 1
    if diagnol2 == 5:
        res += 1
    return res
    
for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        # 붙려진 번호 지우기
        for r in range(5):
            for c in range(5):
                if board[r][c] == arr[j]:
                    board[r][c] = 0
        # 빙고 됐는지 확인
        if bingo() >= 3:
            print(i*5+j+1)
            exit()
            