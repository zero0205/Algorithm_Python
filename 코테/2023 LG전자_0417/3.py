# 1~N개의 나라
# 언어 : 1~ 10번 언어
# 각 나라별로 사용 언어가 다름
# 1번 나라에 사는 A는 k개의 언어를 추가로 배워서 최대 몇개의 나라 방문 가능?
from collections import deque
from itertools import combinations
n, m, k = map(int, input().split())
# i번째 나라에서 사용하는 언어 (1~N)
lan = [0] + list(map(int, input().split()))
road = [[] for _ in range(n+1)]
for _ in range(m):
    p, q = map(int, input().split())
    road[p].append(q)
    road[p].append(q)
    
lan_set = list(set([i for i in range(1, 11)])-lan[1])   # 1번 나라의 언어 일단 제외
ans = 0
for lan_lst in combinations(lan_set, k):    # 사용 언어 리스트
    res = 0
    lan_lst = list(lan_lst) + [lan[1]]
    
    visited = [False] * (n+1)
    visited[1] = True
    q = deque([1])
    while q:
        now = q.popleft()
        for nx in road[now]:
            if not visited[nx] and (lan[nx] in lan_lst):
                q.append(nx)
                visited[nx] = True
                res += 1
    ans = max(ans, res)
print(ans)