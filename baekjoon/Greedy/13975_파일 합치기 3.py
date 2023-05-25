import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify

for _ in range(int(input())):
    k = int(input())
    file = list(map(int, input().split()))
    heapify(file)
    ans = 0
    while len(file) >= 2:
        a = heappop(file)
        b = heappop(file)
        heappush(file, a+b)
        ans += (a+b)
    print(ans)      