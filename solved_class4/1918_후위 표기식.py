notation = input()

stack = []
answer = ""
for c in notation:
    if c == '(':
        stack.append(c)
    elif c == '*' or c == '/':
        while stack and stack[-1] != '(' and (stack[-1] != '+' and stack[-1] != '-'):
            answer += stack.pop()
        stack.append(c)
    elif c == '+' or c == '-':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(c)
    elif c == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop() 
    else:   # 피연산자
        stack.append(c)
        
while stack:
    answer += stack.pop()

print(answer)