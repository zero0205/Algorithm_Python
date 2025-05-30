def xor_calculation(cards):
    result = cards[0]
    for i in range(1, len(cards)):
        result ^= cards[i]
    return bin(result).count("1")


n = int(input())
arr = [0]+list(map(int, input().split()))

if n == 1:
    print(0)
else:
    dp = [0]*(n+1)

    if n >= 2:
        dp[2] = xor_calculation(arr[1:3])
    if n >= 3:
        dp[3] = xor_calculation(arr[1:4])
    if n >= 4:
        dp[4] = dp[2] + xor_calculation(arr[3:5])
    for i in range(5, n+1):
        dp[i] = max(dp[i-2]+xor_calculation(arr[i-1:i+1]),
                    dp[i-3]+xor_calculation(arr[i-2:i+1]))
    print(dp[n])
