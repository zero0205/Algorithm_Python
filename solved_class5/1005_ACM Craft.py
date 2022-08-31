from collections import deque
import sys
input = sys.stdin.readline
    
for _ in range(int(input())):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    
    indegree = [0] * (n+1)  # 모든 노드에 대한 진입차수 0으로 초기화
    graph = [[] for _ in range(n + 1)]
    dp = [0] * (n + 1)  # i번째 건물까지 짓는데 걸리는 최소 시간
    
    # 건설 순서 입력 받기
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    
    w = int(input())
    
    # 위상 정렬       
    # 진입차수 0인 거 큐에 넣기
    q = deque()
    for i in range(1, n + 1): 
        if indegree[i] == 0:
            q.append(i)
            dp[i] = d[i]
    
    while q:
        now = q.popleft()
        for el in graph[now]:
            indegree[el] -= 1
            dp[el] = max(dp[el], dp[now] + d[el])
            
            if indegree[el] == 0:
                q.append(el)

    print(dp[w])