def solution(survey, choices):
    answer = ''
    k_mbti = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i in range(len(survey)):
        if choices[i] > 4:
            k_mbti[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            k_mbti[survey[i][0]] += 4 - choices[i]

    lst = list(k_mbti.keys())
    for idx in range(0, 7, 2):
        if k_mbti[lst[idx]] >= k_mbti[lst[idx + 1]]:
            answer += lst[idx]
        else:
            answer += lst[idx + 1]
    return answer

# 테스트 케이스
print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))

# 정답
# TCMA
# RCJA