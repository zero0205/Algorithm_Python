def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker[0]
    # Case1) 0번 뜯음
    dp = [0 for _ in range(len(sticker))]
    dp[0], dp[1] = sticker[0], sticker[0] 
    for i in range(2, len(sticker)-1):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    answer = dp[-2]
    # Case2) 1번 뜯음(0번 못 뜯음)
    dp.clear()
    dp = [0 for _ in range(len(sticker))]
    dp[0], dp[1] = 0, sticker[1] 
    for i in range(2, len(sticker)):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    return max(answer, dp[-1])