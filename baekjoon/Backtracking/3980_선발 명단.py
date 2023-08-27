import sys
input = sys.stdin.readline

ans = 0


def place(visited, ability, idx, cnt, max_v):
    global ans
    if idx >= 11:
        ans = max(ans, max_v)
        return
    for p in range(11):
        if not visited[p] and ability[idx][p] > 0:
            visited[p] = True
            place(visited, ability, idx+1, cnt+1, max_v+ability[idx][p])
            visited[p] = False


for _ in range(int(input())):
    ability = []
    for i in range(11):
        ability.append(list(map(int, input().split())))
    ans = 0
    visited = [False] * 11
    place(visited, ability, 0, 0, 0)
    print(ans)
