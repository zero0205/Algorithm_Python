import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
    max_q = []
    min_q = []
    alive = [False] * 1000000
    for i in range(int(input())):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':  # 삽입 연산
            heapq.heappush(max_q, (-n, i))
            heapq.heappush(min_q, (n, i))
            alive[i] = True
        else:           # 삭제 연산
            if n == 1:  # 최댓값 삭제
                while max_q and not alive[max_q[0][1]]:    # 이미 삭제된 수들 pop
                    heapq.heappop(max_q)
                if max_q:
                    alive[max_q[0][1]] = False
                    heapq.heappop(max_q)
            else:       # 최솟값 삭제
                while min_q and not alive[min_q[0][1]]:    # 이미 삭제된 수들 pop
                    heapq.heappop(min_q)
                if min_q:
                    alive[min_q[0][1]] = False
                    heapq.heappop(min_q)

    while max_q and not alive[max_q[0][1]]:    # 이미 삭제된 수들 pop
        heapq.heappop(max_q)
    while min_q and not alive[min_q[0][1]]:    # 이미 삭제된 수들 pop
        heapq.heappop(min_q)

    if max_q and min_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print("EMPTY")