import sys
sys.setrecursionlimit(int(1e7))

def dfs(selected, visited, cycle, x):
    global team
    visited[x] = True
    cycle.append(x)
    
    if not visited[selected[x]]:
        dfs(selected, visited, cycle, selected[x])    # 재귀호출
    else:   # 이미 방문한 노드 나옴
        if selected[x] in cycle:
            team += cycle[cycle.index(selected[x]):]
        return

for _ in range(int(input())):
    n = int(input())
    selected = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)   
    
    team = []
    
    for i in range(1, n + 1):
        cycle = []
        if not visited[i]:
            dfs(selected, visited, cycle, i)
    print(n - len(team))