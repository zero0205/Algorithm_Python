from itertools import combinations

def solution(sentences, n):
    answer = -1
    need = [[] for _ in range(len(sentences))]  # 필요한 키들, 점수
    all_key = set()
    for i in range(len(sentences)):
        key = set()
        shift = 0
        for s in sentences[i]:
            if 'A' <= s <= 'Z': # 대문자
                key.add(s.lower())
                key.add("shift")
                shift += 1
            elif s == ' ':
                continue
            else:
                key.add(s)
        need[i] = key, len(sentences[i]) + shift
        all_key = all_key | key

    # 가능한 sentences 인덱스 조합 모두 뽑기 (comb의 길이는 최대 32767)
    comb = []
    for i in range(len(sentences)):
        comb.extend(list(combinations(range(len(sentences)), i)))
        
    for idx_set in comb:
        sum = 0
        need_key = set()
        for idx in idx_set:
            sum += need[idx][1]
            need_key = need_key | need[idx][0]
        if len(need_key) <= n:
            answer = max(answer, sum)
    return answer

print(solution(["line in line", "LINE", "in lion"], 5))
print(solution(["ABcD", "bdbc", "a", "Line neWs"],7))