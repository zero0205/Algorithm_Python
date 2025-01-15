from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))

count_dict = dict()
for i in range(n):
    if arr[i] not in count_dict:
        count_dict[arr[i]] = [i, 1]
    else:
        count_dict[arr[i]][1] += 1

hq = []
for k, v in count_dict.items():
    heappush(hq, [-v[1], v[0], k])

while hq:
    cnt, init, num = heappop(hq)
    for i in range(-cnt):
        print(num, end=" ")
