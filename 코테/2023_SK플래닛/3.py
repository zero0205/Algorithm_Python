# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def flower(board, n, character, cnt):
    if cnt == 0:
        return 1    
    [x, y] = character
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n: # 범위를 벗어나지 않는다면
            if board[nx][ny] == 1:    # 길이라서 꽃 심을 수 있음
                board[nx][ny] = 2
                if flower(board, n, [nx, ny], cnt - 1) == 1:
                    return 1
                else:
                    board[nx][ny] = 1
    return 0
    
def solution(boards):
    answer = []
    for b in boards:
        n = len(b)
        board = [[0] * n for _ in range(n)]
        character = []
        cnt = 0
        for i in range(n):
            for j in range(n):
                board[i][j] = int(b[i][j])
                if board[i][j] == 2:    # 캐릭터 위치 파악
                    character = [i, j]
                if board[i][j] == 1:    # 길의 칸 수 파악
                    cnt += 1
        answer.append(flower(board, n, character, cnt))
    return answer

print(solution([["00011", "01111", "21001", "11001", "01111"], ["00011", "00011", "11111", "12101", "11111"]]))
# [1, 1]
print(solution([["1111", "1121", "1001", "1111"], ["0000", "0000", "0000", "0002"], ["0000", "0100", "0000", "0002"], ["0000", "0010", "0121", "0010"]]))
# [1, 1, 0, 0]