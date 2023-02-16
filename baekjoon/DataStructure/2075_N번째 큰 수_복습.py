import sys, heapq

n = int(sys.stdin.readline())
heap = []   # 표에서 큰 수 N개를 저장할 힙
for _ in range(n):
    for i in list(map(int, sys.stdin.readline().split())):
        # 힙에 N개만큼 차지 않았다면 그냥 push
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            # 지금 힙에 있는 최솟값보다 현재 들어온 값이 더 크다면
            # heap의 최솟값 pop해버리고 현재 값 넣어줌
            if heap[0] < i: 
                heapq.heappop(heap)
                heapq.heappush(heap, i)
# 최종적으로 힙에서 가장 작은 값이 표에서 N번째 큰 수
print(heap[0])