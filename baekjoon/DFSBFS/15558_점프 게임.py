from collections import deque

n, k = map(int, input().split())
game_map = []
for _ in range(2):
    game_map.append("0"+input())

q = deque([(0, 1, 1)])
visited = [[False]*(n+1) for _ in range(2)]
visited[0][1] = True
while q:
    line, num, sec = q.popleft()
    for nx_line, nx_num in [(line, num+1), (line, num-1), (line ^ 1, num+k)]:
        if nx_num > n:
            print(1)
            exit()
        if 0 <= nx_num <= n and game_map[nx_line][nx_num] == "1" and nx_num > sec and not visited[nx_line][nx_num]:
            q.append((nx_line, nx_num, sec+1))
            visited[nx_line][nx_num] = True
print(0)
