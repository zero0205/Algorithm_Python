import sys, heapq
from collections import defaultdict

for _ in range(int(sys.stdin.readline())):
    min_heap = []
    max_heap = []
    num = defaultdict(int)
    for i in range(int(sys.stdin.readline())):
        cmd, n = sys.stdin.readline().split()   # 연산을 나타내는 문자, 정수
        n = int(n)
        if cmd == "I":  # 삽입 연산
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            num[n] += 1
        else:           # 삭제 연산
            if n == 1:  # 큐에서 최댓값 삭제
                while max_heap and num[-max_heap[0]] == 0:  # 이미 삭제된 숫자이면 pop해줌
                    heapq.heappop(max_heap)
                if max_heap:
                    num[-heapq.heappop(max_heap)] -= 1
            else:       # 큐에서 최솟값 삭제
                while min_heap and num[min_heap[0]] == 0:  # 이미 삭제된 숫자이면 pop해줌
                    heapq.heappop(min_heap)
                if min_heap:
                    num[heapq.heappop(min_heap)] -= 1          
                    
    while max_heap and num[-max_heap[0]] <= 0:
        num[-heapq.heappop(max_heap)] -= 1
    while min_heap and num[min_heap[0]] <= 0:
        num[heapq.heappop(min_heap)] -= 1
        
    if max_heap and min_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")