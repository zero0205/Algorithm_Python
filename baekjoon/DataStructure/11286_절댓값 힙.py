import sys, heapq

max_heap = []
cnt = 0
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x == 0:
        print(heapq.heappop(max_heap)[1] if max_heap else 0)
    else:
        heapq.heappush(max_heap, (abs(x), x))