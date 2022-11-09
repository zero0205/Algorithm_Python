from collections import deque

def is_right(s):
    stack = []
    
    for i in s:
        if i == '[' or i == '{'or i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                if i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
    return (False if stack else True)

def solution(s):
    answer = 0
    q = deque(s)
    for i in range(len(s)):
        if is_right(q):
            answer += 1
        head = q.popleft()
        q.append(head)
    return answer