# https://programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict

def solution(gems):
    n = len(gems)
    size = len(set(gems))
    
    answer = [0, n - 1]
    
    now_gems = defaultdict(int)
    start, end = 0, 0
    now_gems[gems[start]] = 1
    while start < n and end < n:
        if len(now_gems) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            # start 인덱스 지점의 보석 하나 뺼거임
            if now_gems[gems[start]] - 1 == 0:    
                del now_gems[gems[start]]
            else:
                now_gems[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == n:
                break
            now_gems[gems[end]] += 1
    return [answer[0] + 1, answer[1] + 1]

# 테스트 케이스
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))