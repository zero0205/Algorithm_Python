n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

def dfs(i, arr_sum):
    global ans
    
    if i >= n:
        return
    
    arr_sum += arr[i]
    if arr_sum == s:
        ans += 1
        
    dfs(i+1, arr_sum-arr[i])
    dfs(i+1, arr_sum)
   
dfs(0, 0)
print(ans)