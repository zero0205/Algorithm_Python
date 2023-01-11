from collections import deque
# skill : 선행 스킬 순서
# skill_trees : 유저들이 만든 스킬트리를 만든 배열
def solution(skill, skill_trees):   
    answer = 0
    for i in range(len(skill_trees)):
        skill_deq  = deque(list(skill))
        flag = True
        for s in skill_trees[i]:
            if not skill_deq:
                break
            if s == skill_deq[0]:
                skill_deq.popleft()
            else:
                if s in skill_deq:
                    flag = False
        if flag:
            answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
# 2