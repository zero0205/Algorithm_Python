def get_boss(p, n):
    if p[n] == -1:
        return n
    else:
        p[n] = get_boss(p, p[n])
    return p[n]

def solution(p, b):
    answer = []
    # 각 조직원들의 최종 보스 표시
    for i in range(len(p)):
        get_boss(p, i)
    # 조직원 수 구하기
    for i in b:
        if p[i] != -1:  # 최종 보스가 아니라면
            answer.append(0)
            continue
        cnt = 0
        for j in range(len(p)):
            if i == p[j]:   # 조직원이라면
                cnt += 1
            else:
                if p[j] == -1 and i == j:   # 최종 보스
                    cnt += 1
        answer.append(cnt) 
    return answer

print(solution([2, 2, -1, 1, 5, -1, 5], [2, 5]))
# [4, 3]
print(solution([2, 2, -1, 1, 5, -1, 5], [1, 5]))
# [0, 3]