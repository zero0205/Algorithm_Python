# https://www.acmicpc.net/problem/4949

while True:
    q = []
    s = input()
    
    if s == '.':
        break
    
    for c in s:
        if c == '[' or c == '(':
            q.append(c)
        elif c == ']':
            if q and q[-1] == '[':
                q.pop()
            else:
                q.append(c)
                break
        elif c == ')':
            if q and q[-1] == '(':
                q.pop()
            else:
                q.append(c)
                break
        else:
            continue
    if q:   # 스택에 남은 괄호들이 있다면 짝이 안 맞는거
        print("no")
    else:
        print("yes")