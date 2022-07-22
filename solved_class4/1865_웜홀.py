import sys
input = sys.stdin.readline

# 벨만 포드 알고리즘
# 최단 거리 테이블이 갱신된다면 음수 간선 사이클이 있는 것
def bf(start):
    dist[start] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):   
            for nx, t in road[j]:   # 벨만포드는 모든 간선 다 확인
                if dist[nx] > dist[j] + t:   # 지금 노드를 통해 가는게 더 시간이 단축된다면
                    dist[nx] = dist[j] + t
                    if i == n:  # n번 했는데도 갱신되면 음의 사이클 존재
                        return True

tc = int(input())   # 테스트케이스의 개수

for i in range(tc):
    n, m, w = map(int, input().split())
    
    road = [[] for _ in range(n + 1)]
    dist = [10001 for _ in range(n + 1)]
  
    # 도로의 정보 입력
    for _ in range(m): 
        s, e, t = map(int, input().split())
        road[s].append((e,t))
        road[e].append((s,t))
    # 웜홀의 정보 입력
    for _ in range(w):
        s, e, t = map(int, input().split())
        road[s].append((e,-t))       

    if bf(1):
        print("YES")
    else:
        print("NO")