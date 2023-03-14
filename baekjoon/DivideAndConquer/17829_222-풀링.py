import sys, heapq
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
    
def pooling(n):
    if n == 1:
        print(arr[0][0])
        return
    deq = deque()
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            # 2X2 정사각형에서 2번째로 큰 수 찾기
            heap = []
            for p in range(i, i+2):
                for q in range(j, j+2):
                    heapq.heappush(heap, -arr[p][q])
            heapq.heappop(heap)
            deq.append(-heapq.heappop(heap)) # 2번째로 큰 수 deq에 append
    # 2번째로 큰 수들 arr에 갱신
    for i in range(n//2):
        for j in range(n//2):
            arr[i][j] = deq.popleft()
    pooling(n//2)
    
pooling(n)