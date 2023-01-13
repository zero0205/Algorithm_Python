import re
from itertools import permutations

def match(u_id, b_id):
    for i in range(len(b_id)):
        p = re.compile(b_id[i])
        # 문자열 일치하는지 정규표현식으로 확인
        if len(u_id[i]) != len(b_id[i]) or not p.match(u_id[i]):   
            return False
    return True
    
def solution(user_id, banned_id):
    answer = []
    banned_id_re = []
    # 정지 아이디 정규표현식으로 만들어서 리스트 생성
    for i in banned_id:
        banned_id_re.append(i.replace('*', '.'))
    # 가능한 모든 유저 아이디 조합에 대해 모두 정지될 수 있는 아이디 리스트인지 확인
    for i in permutations(user_id, len(banned_id)):
        if match(i, banned_id_re):
            i = set(i)
            if i not in answer:
                answer.append(i)
    return len(answer)

# 테스트 케이스
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))