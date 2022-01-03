# 구현
# 2. 게임 개발

# 맵 생성 (n : 세로, m : 가로, 3 <= n,m <= 50)
n, m = map(int, input().split())

# 캐릭터 위치 입력 (방향 => 0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽)
x, y, d = input().split()

# 맵 정보 입력
map = []
for i in range(n):
    map[i] = list(map(int, input().split()))

cnt = 0
is_move = False

# 한 칸 전진(서 남 동 북)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 가봤는지 체크하는 맵 생성
map_check = [[0 for col in range(m)] for row in range(n)]

# 뒤쪽이 바다라서 뒤로 갈 수 없는 상황이 올 때까지 반복
while True:
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        # 맵 범위 내인가?
        if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
            continue
        # 바다인가?
        if map[next_x][next_y] == 1:
            continue
        # 이미 가본 칸인가?
        if map_check[next_x][next_y] == 1:
            continue

        x = next_x
        y = next_y
        map_check[x][y] = 1
        cnt += 1
        is_move = True

    if is_move:
        continue

    