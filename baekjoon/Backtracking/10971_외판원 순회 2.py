n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))
    
visited = [False] * n
min_cost = int(1e9)

def dfs(idx, cnt, cost_sum):
    global min_cost
    if cnt == n:
        if cost[idx][0] != 0:
            min_cost = min(min_cost, cost_sum+cost[idx][0])
        return
    for i in range(n):
        if not visited[i] and cost[idx][i] != 0:
            visited[i] = True
            dfs(i, cnt+1, cost_sum+cost[idx][i])
            visited[i] = False
            
visited[0] = True
dfs(0, 1, 0)
print(min_cost)