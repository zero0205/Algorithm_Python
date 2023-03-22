n = int(input())
cost = []
min_cost = int(1e9)
visited = [False] * n
for _  in range(n):
    cost.append(list(map(int, input().split())))
    
def dfs(now, now_cost, visited_cities_num):
    global min_cost
    if visited_cities_num == n: # 도시들을 모두 방문
        if cost[now][0] != 0:   # 마지막 도시에서 처음 출발한 도시(0)으로 갈 수 있는 경우
            min_cost = min(min_cost, now_cost+cost[now][0])
        return
    # 다 방문하지도 않았는데 이미 비용은 최소 비용보다 크면 더 볼 필요 없음
    if now_cost > min_cost: 
        return
    for i in range(n):
        if not visited[i] and cost[now][i] != 0:
            visited[i] = True
            dfs(i, now_cost+cost[now][i], visited_cities_num+1)
            visited[i] = False
            
visited[0] = True
dfs(0, 0, 1)
print(min_cost)