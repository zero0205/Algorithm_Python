from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
big, small = [], []
for _ in range(n):
    num = int(input())
    if len(small) == len(big):
        heappush(small, -num)
    else:
        heappush(big, num)
    # small 중 가장 큰 수 > big 중 가장 작은 수
    if big and -small[0] > big[0]:
        b = heappop(big)
        s = -heappop(small)
        heappush(big, s)
        heappush(small, -b)
    print(-small[0])
