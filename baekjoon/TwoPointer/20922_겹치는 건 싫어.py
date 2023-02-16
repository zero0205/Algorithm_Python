from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
    
start, end = 0, 0

max_length = 1
num_cnt = defaultdict(int)
while end < n:
    if num_cnt[arr[end]] < k:
        num_cnt[arr[end]] += 1
        end += 1
    else:
        num_cnt[arr[start]] -= 1
        start += 1
    max_length = max(max_length, end-start)
print(max_length)