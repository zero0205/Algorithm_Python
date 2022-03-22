# https://www.acmicpc.net/problem/11286

import heapq, sys

n = int(input())

q = []
for _ in range(n):
    input_data = int(sys.stdin.readline())
    if input_data == 0:
        if q:
            pop_data = heapq.heappop(q)
            arr = [pop_data]
            while True:
                if not q:
                    break
                pop_data = heapq.heappop(q)
                if pop_data[0] == arr[0][0]:
                    arr.append(pop_data)
                else:
                    heapq.heappush(q, pop_data)
                    break
            arr.sort(key=lambda x:x[1])
            print(arr[0][1])            
            
            for el in arr[1:]:
                heapq.heappush(q, el)
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(input_data), input_data))