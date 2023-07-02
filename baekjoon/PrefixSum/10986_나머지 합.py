import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pfSum = 0
mod_lst = [0] * m
for i in range(n):
    pfSum += arr[i]
    mod_lst[pfSum % m] += 1

ans = 0
for i in mod_lst:
    ans += i * (i-1) // 2
print(ans + mod_lst[0])