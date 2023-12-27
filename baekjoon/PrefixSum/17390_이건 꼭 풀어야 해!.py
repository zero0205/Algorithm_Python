import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(a)   # 비내림차순 정렬

# 누적합
prefix_sum = [0]*(n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1]+b[i-1]

for _ in range(q):
    l, r = map(int, input().split())
    print(prefix_sum[r]-prefix_sum[l-1])
