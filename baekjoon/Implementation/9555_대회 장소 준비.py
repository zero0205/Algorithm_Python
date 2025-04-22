import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(int(input())):
    n, m = map(int, input().split())
    teams = [list(map(int, input().split())) for _ in range(n)]

    answer = set()
    for x in range(n):
        for y in range(m):
            if teams[x][y] == -1 or teams[x][y] in answer:
                continue
            for d in range(8):
                nx = x+dx[d]
                ny = y+dy[d]
                if 0 <= nx < n and 0 <= ny < m and teams[nx][ny] == teams[x][y]:
                    answer.add(teams[x][y])
                    break
    print(len(answer))
