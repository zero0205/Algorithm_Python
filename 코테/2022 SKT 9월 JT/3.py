from collections import defaultdict

def solution(s, word_dict):
    answer = 0

    len_dict = defaultdict(list)
    for word in word_dict:
        len_dict[len(word)].append(word)

    dp = [0] * len(s)
    is_end = [False] * len(s)
    is_end[0] = True

    for i in range(2, len(s)+1):
        for k in range(2, 11): # 단어의 길이
            if s[i-k:i] in len_dict[k]:
                if is_end[i-k]:
                    dp[i-1] = max(dp[i-1], dp[i-k] + 1)
                    is_end[i-1] = True
                else:
                    dp[i-1] = max(dp[i-1], dp[i-k])
            else:
                dp[i-1] = max(dp[i-1], dp[i-k])

    return dp[-1]