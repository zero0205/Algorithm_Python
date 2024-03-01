for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    # 누적합
    preSum = [0]
    for i in range(n):
        preSum.append(preSum[-1]+x[i])
    # 브루트포스
    ans = -int(1e9)
    for l in range(n):
        for r in range(l+1, n+1):
            if preSum[r]-preSum[l] > ans:
                ans = preSum[r]-preSum[l]
    print(ans)
