# 구현
# 2. 게임 개발

# 맵 생성 (n : 세로, m : 가로, 3 <= n,m <= 50)
n, m = map(int, input().split())

# 캐릭터 위치 입력 (방향 => 0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽)
x, y, d = map(int, input().split())

# 맵 정보 입력
input_map = []
for i in range(n):
    input_map.append(list(map(int, input().split())))

cnt = 1
turn = 0

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 가봤는지 체크하는 맵 생성
map_check = [[0 for col in range(m)] for row in range(n)]

# 현재 좌표 방문 처리
map_check[x][y] = 1

# 왼쪽으로 회전
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

# 뒤쪽이 바다라서 뒤로 갈 수 없는 상황이 올 때까지 반복
while True:
    turn_left()
    next_x = x + dx[d]
    next_y = y + dy[d]

    # 갈 수 있는 칸인가?
    if input_map[next_x][next_y] == 0 and map_check[next_x][next_y] == 0:
        x = next_x
        y = next_y
        map_check[x][y] = 1
        cnt += 1
        turn = 0
        continue
    else:
      turn += 1

    # 네 방향 모두 못 가는 상황
    if turn == 4:
        next_x = x - dx[d]
        next_y = y - dy[d]

        # 뒤로 갈 수 있음?
        if input_map[next_x][next_y] == 0:
            x = next_x
            y = next_y
        else:
            break

        turn = 0    

print(cnt)