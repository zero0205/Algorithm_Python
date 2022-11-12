from collections import defaultdict
def solution(reference, track):
    answer = 0
    d = defaultdict(list)
    for length in range(1, len(reference)+1):
        for i in range(len(reference)-length):
            d[length].append(reference[i:i+length])

    dp = [0 for _ in range(len(track))]
    for i in range(len(track)):
        for j in range(i):  # 점프문자열 길이
            if track[i-j+1:i+1] in d[j]:    # 점프 가능
                dp[i] = max(dp[i-j+1], j)
    return dp[-1]

print(solution("abc","bcab"))
# 2
print(solution("vxrvip","xrviprvipvxrv"))
# 4