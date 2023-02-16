import sys, heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    for i in list(map(int, sys.stdin.readline().split())):
        # 힙에 이미 n개의 원소가 있을 때 
        # 힙에서 가장 작은 원소와 비교하여 
        # 더 크면 가장 작은 원소 pop해버리고 본인이 들어감
        if len(heap) == n:  
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        else:   # 아직 힙에 n개의 원소보다 덜 찼을 때는 그냥 push
            heapq.heappush(heap, i)
            
print(heap[0])