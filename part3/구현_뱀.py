from collections import deque

# 회전
def turn(now, dir): # 현재 방향과 회전할 방향을 인자로 받음
    turn_dir = [(0,1),(1,0),(0,-1),(-1,0)] # 우 하 좌 상
    idx = turn_dir.index(now)
    
    #회전할 방향에 따라 다음 방향 반환
    if dir == 'L':  # 왼쪽으로 회전
        idx -= 1
    elif dir == 'D':    # 오른쪽으로 회전
        idx += 1
    # 인덱스가 0 ~ 3을 벗어나지 않도록
    if idx < 0:
        idx = 3
    elif idx > 3:
        idx = 0
    # 뱀이 향할 방향 반환
    return turn_dir[idx] 

# 보드 크기 n 입력받기
n = int(input())
# 사과 개수 k 입력 받기
k = int(input())
# 사과 위치 입력 받기
board = [[0 for col in range(n + 1)] for row in range(n + 1)]   # 보드 초기화
for _ in range(k):
    row, col = map(int, input().split())
    board[row][col] = 1 # 사과가 있는 위치는 1, 없으면 0
   
now_dir = (0, 1)    # 처음에는 오른쪽을 향함
# 방향 변환 횟수 l 입력받기
l = int(input())
# 방향 변환 정보 입력받기
move = deque([])
for _ in range(l):
    # move 배열에 방향 변환 정보 튜플 형태로 저장
    move.append(tuple(input().split())) 
    
# 뱀이 위치하고 있는 칸(왼쪽이 꼬리, 오른쪽이 머리)
snake = deque([(1,1)])    
t = 0   # 게임 진행 시간
move_timing = move.popleft()    # 방향 전환 타임 체크용
while True:
    t += 1  # 시간 증가
    # 머리 이동 위치
    row = snake[len(snake)-1][0] + now_dir[0]
    col = snake[len(snake)-1][1] + now_dir[1]
    
    # 벽과 부딪힘
    if row <= 0 or row > n or col <= 0 or col > n:
        break
    # 몸통과 부딪힘
    if (row, col) in snake:
        break
    # 방향 전환 타임?
    if t == int(move_timing[0]):
        now_dir = turn(now_dir, move_timing[1])
        if move:
            move_timing = move.popleft()
        
    snake.append((row, col))    # snake 배열에 추가
    
    # 지금 자리에 사과 있으면 사과 먹고 꼬리 안 움직임
    if board[row][col] == 1:
        board[row][col] = 0 # 사과 냠냠
        continue
    else:   # 이동한 칸에 사과 없음
        snake.popleft() # 꼬리 치워
        
print(t)