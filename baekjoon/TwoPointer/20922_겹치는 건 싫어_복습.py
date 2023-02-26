from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

num_cnt = defaultdict(int)
start, end = 0, 0
ans = 0
while end < n:
    if num_cnt[arr[end]] >= k:
        num_cnt[arr[start]] -= 1
        start += 1
    else:
        num_cnt[arr[end]] += 1
        end += 1
    ans = max(ans, end-start)
    
print(ans)