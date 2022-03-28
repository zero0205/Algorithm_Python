# 시계방향 (우 하 좌 상)
dx_clock = [0, 1, 0, -1]
dy_clock = [1, 0, -1, 0]
# 반시계 방향 (하 우 상 좌)
dx_nonclock = [1, 0, -1, 0]
dy_nonclock = [0, 1, 0, -1]

def print_map(map_data):
    for row in map_data:
        for col in row:
            print(col, end=' ')
        print()
        
def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    # 네 귀퉁이에서 동시에 시작. 이미 채워진 칸을 만나면 turn
    num = 1
    x1, y1 = 0, 0
    x2, y2 = ((0, n - 1) if clockwise else (n - 1, 0))
    x3, y3 = n - 1, n - 1
    x4, y4 = ((n - 1, 0) if clockwise else (0, n - 1))
    dir = 0
    while True: 
        if answer[x1][y1] != 0:
            break
        answer[x1][y1] = answer[x2][y2] = answer[x3][y3] = answer[x4][y4] = num
        if clockwise:   # 시계 방향
            nx1, ny1 = x1 + dx_clock[dir % 4], y1 + dy_clock[dir % 4] 
            if answer[nx1][ny1] != 0:   # 이미 채워진 칸이라면 turn
                dir += 1
            x1, y1 = x1 + dx_clock[dir % 4], y1 + dy_clock[dir % 4]
            x2, y2 = x2 + dx_clock[(dir + 1) % 4], y2 + dy_clock[(dir + 1) % 4]
            x3, y3 = x3 + dx_clock[(dir + 2) % 4], y3 + dy_clock[(dir + 2) % 4]
            x4, y4 = x4 + dx_clock[(dir + 3) % 4], y4 + dy_clock[(dir + 3) % 4]
        else:
            nx1, ny1 = x1 + dx_nonclock[dir % 4], y1 + dy_nonclock[dir % 4]
            if answer[nx1][ny1] != 0:   # 이미 채워진 칸이라면 turn
                dir += 1
            x1, y1 = x1 + dx_nonclock[dir % 4], y1 + dy_nonclock[dir % 4]
            x2, y2 = x2 + dx_nonclock[(dir + 1) % 4], y2 + dy_nonclock[(dir + 1) % 4]
            x3, y3 = x3 + dx_nonclock[(dir + 2) % 4], y3 + dy_nonclock[(dir + 2) % 4]
            x4, y4 = x4 + dx_nonclock[(dir + 3) % 4], y4 + dy_nonclock[(dir + 3) % 4]
        num += 1
        
    return answer

# 출력용
n, c = map(int, input().split())
c = (True if c == 1 else False)

ans = solution(n, c)

for i in ans:
    for j in i:
        print(j, end='  ')
    print()
