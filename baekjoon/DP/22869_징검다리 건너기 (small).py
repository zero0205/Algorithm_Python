n, k = map(int, input().split())
stone = list(map(int, input().split()))
dp = [False] * n
dp[0] = True
for j in range(1, n):
    for i in range(j):
        if not dp[i] or dp[j]:  # i번째 돌이 올 수 없는 돌이거나 j번째가 이미 올 수 있음이 확인된 경우
            continue
        energy = (j-i) * (1+abs(stone[i]-stone[j]))
        if energy > k:  # 쓸 수 있는 최대 힘보다 힘이 더 필요해서 못 감
            continue
        dp[j] = True    
print("YES" if dp[n-1] else "NO")