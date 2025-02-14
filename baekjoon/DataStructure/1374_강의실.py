from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
lectures = []
for _ in range(n):
    _, start, end = map(int, input().split())
    lectures.append((start, end))

lectures.sort()

needs = []
for i in range(n):
    start, end = lectures[i]
    if needs and needs[0] <= start:
        heappop(needs)
    heappush(needs, end)
print(len(needs))
