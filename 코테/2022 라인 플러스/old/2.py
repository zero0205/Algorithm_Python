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
    possible = list(combinations(all_key, n))
    for p in possible:
        k = set(p)
        temp = 0
        for n in need:
            if len(k & n[0]) == len(n[0]):
                temp += n[1]
        answer = max(answer, temp)
    return answer

print(solution(["line in line", "LINE", "in lion"],5))
print(solution(["ABcD", "bdbc", "a", "Line neWs"],7))