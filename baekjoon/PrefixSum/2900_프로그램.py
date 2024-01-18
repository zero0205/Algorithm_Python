from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
x_lst = list(map(int, input().split()))
x_dict = defaultdict(int)
for x in x_lst:
    x_dict[x] += 1
# something 함수
a = [0]*n
for jumping, num in x_dict.items():
    for i in range(0, n, jumping):
        a[i] += num
# 누적합
ps = [0] * (n+1)
for i in range(1, n+1):
    ps[i] = ps[i-1]+a[i-1]
q = int(input())

for _ in range(q):
    l, r = map(int, input().split())
    print(ps[r+1]-ps[l])
