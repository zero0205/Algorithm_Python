from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
hard = []
easy = []
included = [[False] for _ in range(100001)]
for _ in range(n):
    p, l = map(int, input().split())
    heappush(hard, (-l, -p))
    heappush(easy, (l, p))
    included[p] = True

m = int(input())
for _ in range(m):
    cmd = input().split()
    # 출력
    if cmd[0] == "recommend":
        # 가장 어려운 문제 번호 출력(1)
        if cmd[1] == "1":
            while not included[-hard[0][1]]:
                heappop(hard)
            print(-hard[0][1])
        # 가장 쉬운 문제 번호 출력(-1)
        else:
            while not included[easy[0][1]]:
                heappop(easy)
            print(easy[0][1])
    # 추가
    elif cmd[0] == "add":
        while not included[-hard[0][1]]:
            heappop(hard)
        while not included[easy[0][1]]:
            heappop(easy)
        heappush(hard, (-int(cmd[2]), -int(cmd[1])))
        heappush(easy, (int(cmd[2]), int(cmd[1])))
        included[int(cmd[1])] = True
    # 삭제
    else:
        included[int(cmd[1])] = False
