import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    s, t = map(int, input().split())
    classes.append([s, t])

classes.sort()
used = []
for i in range(n):
    if used and used[0] <= classes[i][0]:
        heappop(used)
    heappush(used, classes[i][1])

print(len(used))
