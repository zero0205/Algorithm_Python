import sys
input = sys.stdin.readline

n = int(input())
like = [[] for _ in range(n**2+1)]
board = [[0] * n for _ in range(n)]

# 상좌우하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 인접한 칸에 좋아하는 학생이 몇 명 있는지, 빈 칸 몇 개인지 확인
def get_like(student, x, y):
    res = 0
    blank = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:  # 빈 칸
                blank += 1
                continue
            if board[nx][ny] in like[student]:  # 인접한 칸이 좋아하는 학생이라면
                res += 1     
    return [res, blank]

def find_pos(student):
    like = 0
    blank = 0
    res = []
    # board 전체를 탐색하며 들어갈 위치 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:    # 이미 자리 주인 있음
                continue
            now_like, now_blank = get_like(student, i, j)
            if now_like == 4:   # 인접한 칸이 모두 호감 학생
                return [i, j]
            if now_like > like: 
                res = [i, j]
                like = now_like
                blank = now_blank
                continue
            if now_like == like: 
                if blank < now_blank:   # 인접한 칸에 빈 칸이 더 많은 경우
                    res = [i, j]
                    blank = now_blank
            if not res:
                res = [i, j]
    return res
        
for _ in range(n**2):
    student, *arr = map(int, input().split())
    like[student] = arr
    x, y = find_pos(student)
    board[x][y] = student
    
# 만족도 조사
ans = 0
score = [0, 1, 10, 100, 1000]
for i in range(n):
    for j in range(n):
        ans += score[get_like(board[i][j], i, j)[0]]
    
print(ans)