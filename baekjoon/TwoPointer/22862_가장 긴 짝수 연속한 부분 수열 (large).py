n, k = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
num_odd = 0
ans = 0
while end < n:
    if num_odd <= k:
        if arr[end] % 2 == 1:   # end의 값이 홀수라면
            num_odd += 1
        end += 1
    else:
        if arr[start] % 2 == 1:
            num_odd -= 1
        start += 1
    ans = max(ans, end-start-num_odd)
    
print(ans)