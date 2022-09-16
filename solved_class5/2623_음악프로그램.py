from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n + 1)    # 진입차수
num = 0
ans = []
for _ in range(m):
    singer = list(map(int, input().split()))
    for i in range(2, singer[0]+1):
        indegree[singer[i]] += 1    # 진입차수 + 1
        graph[singer[i-1]].append(singer[i])
        
q = deque([])
# 진입차수가 0인 것들을 큐에 삽입
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        num += 1

# 모든 노드를 방문하기 전에 큐가 빈다면 사이클이 발생하는 것
while q:
    now = q.popleft()
    ans.append(now)
    for i in graph[now]:
        indegree[i] -= 1    # 진입차수 1 감소
        if indegree[i] == 0:    # 진입차수가 0이 된 노드라면 큐에 추가
            q.append(i)
            num += 1
                
if num == n:
    for i in ans:
        print(i)
else:
    print(0)