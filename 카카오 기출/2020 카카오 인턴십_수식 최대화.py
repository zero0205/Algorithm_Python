# https://programmers.co.kr/learn/courses/30/lessons/67257

from collections import deque
from itertools import permutations

def operation(a, b, op):
    if op == "*":
        return a * b
    elif op == "+":
        return a + b
    else:
        return a - b

# 우선순위에 따라 수식 처리해주는 함수
def calc(op_lst, expression):
    s = deque([])
    num = ''
    # 식을 스택으로 처리
    for i in range(len(expression)):
        if expression[i].isdigit():
            num += expression[i]
        else:
            s.append(int(num))   # 숫자 저장
            s.append(expression[i]) # 연산자 저장
            num = ''
    s.append(int(num))   # 마지막 숫자 처리

    for op in op_lst:
        s2 = deque([])
        while s:
            now = s.popleft()
            if now == op:   # 이번에 처리될 연산자
                s2.append(operation(s2.pop(), s.popleft(), op))
            else:
                s2.append(now)
        s = s2
    return abs(s.pop())        
    
def solution(expression):
    answer = 0
    op_lst = ["*", "+", "-"]
    # calc(op_lst, expression)
    for priority in list(permutations(op_lst, 3)):
        answer = max(answer, abs(calc(priority, expression)))
    return answer

# 테스트 케이스
print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))