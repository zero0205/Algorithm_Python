# https://programmers.co.kr/learn/courses/30/lessons/60058

# '올바른 문자열'인지 확인
def check_right(p):
    cnt = 0 # '('의 개수
    if p[0] == ')': # 첫번째가 ')'이면 이미 글렀음
        return False
    # 짝 맞는지 확인
    for i in p:
        if cnt < 0 :
            return False
        if i == '(':    # '('인 경우
            cnt += 1
        else:  # ')'인 경우
            cnt -= 1
    return True

# 4-4 단계 수행 함수
def trim_reverse(p):
    new_str = ""
    for i in p[1:-1]:
        if i == '(':
            new_str += ')'
        else:
            new_str += '('
    return new_str

def dfs(p):
    if len(p) == 0:
        return ""
    if check_right(p):
        return p
    
    while len(p) > 0:
        cnt_l = 0
        cnt_r = 0
        if p[0] == '(':
            cnt_l += 1
        else:
            cnt_r += 1
        while cnt_l != cnt_r:
            if p[cnt_l + cnt_r] == '(':
                cnt_l += 1
            else:
                cnt_r += 1
        u = p[:cnt_l + cnt_r]
        v = p[cnt_l + cnt_r:]
        # u가 올바른 문자열이면
        if check_right(u):
            return u + dfs(v)
        else:
            new_p = '(' + dfs(v) + ')'
            return new_p + trim_reverse(u)
    
def solution(p):
    answer = ''
    answer = dfs(p)
            
    return answer

my_str = input()
print(solution(my_str))