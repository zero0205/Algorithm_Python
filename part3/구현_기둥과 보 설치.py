def check1(board, job):  # 기둥 설치/삭제 가능?
    x, y = job[0], job[1]  # x, y 좌표
    if job[3] == 0: # 삭제
        # 위에 기둥이나 보가 있으면 삭제 불가
        if board[x][y+1] == 3 or board[x][y] == 4:
            return False
        return True
    elif job[3] == 1: # 설치
        if job[1] == 0: # 바닥이니까 설치 가능
            return True
        if board[x][y] == 1 or board[x][y] == 2: # 기둥 또는 보 위
            return True
        return False

def check2(board, job): # 보 설치/삭제 가능?
    x, y = job[0], job[1]  # x, y 좌표
    if job[3] == 0: # 삭제
        # 위에 기둥 있으면 삭제 불가
        if board[x][y] == 4 or board[x + 1][y] == 4:
            return False
        # 이거 삭제하면 옆에 보가 떨어지는 경우 삭제 불가
        if board[x][y] == 5 and board[x + 1][y] == 5:
            return False
        return True
    elif job[3] == 1: # 설치
        if job[1] == 0: # 바닥이면 설치 불가
            return False
        if board[x][y] == 1 or board[x+1][y] == 1:      # 기둥 위
            return True
        if board[x][y] == 2 and board[x + 1][y] == 2:   # 보-보-보
            return True
        return False

def solution(n, build_frame):
    answer = [[]]
    # 아무것도 없음: 0, 기둥: 1, 보: 2, 기둥/기둥: 3, 기둥/보: 4, 보/보: 5
    board = [[0] * (n + 1) for _ in range(n + 1)]   # 보드 초기화
    for job in build_frame:
        x, y = job[0], job[1]  # x, y 좌표
        a = job[2]  # 구조물 종류 (0:기둥, 1:보)
        b = job[3]  # 작업 종류   (0:삭제, 1:설치)
        
        if a == 0:  # 기둥
            if not check1(board, job):  # 설치/삭제 불가
                continue
            else:
                if b == 0:  # 기둥 삭제
                    board[x][y + 1] = 0 # 위에 아무것도 없는거니까 위는 그냥 0으로
                    if board[x][y] == 3:    # 기둥 밑이 기둥
                        board[x][y] = 1
                    elif board[x][y] == 4:  # 기둥 밑이 보
                        board[x][y] = 2
                    else:   # 기둥 밑과 연결된 구조물 없음
                        board[x][y] = 0
                        
                else:   # 기둥 설치
                    board[x][y + 1] = 1 # 위에 아무것도 없을테니까
                    if board[x][y] == 1:    # 기둥 밑이 기둥
                        board[x][y] = 3
                    elif board[x][y] == 2:  # 기둥 밑이 보
                        board[x][y] = 4
                    else:   # 기둥 밑과 연결된 구조물 없음
                        board[x][y] = 1
        else:   # 보
            if not check2(board, job):  # 설치/삭제 불가
                continue
            else:
                if b == 0:  # 보 삭제
                    if board[x][y] == 4:    # 왼쪽이 기둥과 연결
                        board[x][y] = 1
                    if board[x][y + 1] == 4:    # 오른쪽이 기둥과 연결
                        board[x][y + 1] = 1
                    if board[x][y] == 5:    # 왼쪽이 보와 연결
                        board[x][y] = 2
                    if board[x][y + 1] == 5:    # 오른쪽이 보와 연결
                        board[x][y + 1] = 2                        
                else:   # 보 설치
                    if board[x][y] == 1:    # 왼쪽 밑이 기둥
                        board[x][y] = 4
                    if board[x][y + 1] == 1:    # 오른쪽 밑이 기둥
                        board[x][y + 1] = 4
                    if board[x][y] == 2:    # 왼쪽이 보
                        board[x][y] = 5       
                    if board[x][y + 1] == 2:    # 오른쪽이 보
                        board[x][y + 1] = 5  
    return answer