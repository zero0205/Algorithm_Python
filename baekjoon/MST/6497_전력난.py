import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:   # 입력의 끝
        break
    
    roads = [[] for _ in range(m)]  
    total_cost = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        roads[x].append((z, y))
        roads[y].append((z, x))
        total_cost += z

    mst = set()
    mst.add(0)
    mst_cost = 0
    candidate = roads[0]    # 다음 노드 후보 배열
    heapify(candidate)  # 후보 배열 최소힙으로 만들어주기
    # 프림 알고리즘
    while candidate:
        cost, nx = heappop(candidate)
        if nx not in mst:   # 이전 단계에 만들어진 mst에 포함 안되어 있다면 합격
            mst.add(nx)
            mst_cost += cost
            
            for road in roads[nx]:  # 다음 후보군
                if road[1] not in mst:
                    heappush(candidate, road)
        if len(mst) == m:
            break
    print(total_cost - mst_cost)