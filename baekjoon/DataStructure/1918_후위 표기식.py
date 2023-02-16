input_data = input()

operator = []
for ch in input_data:
    if ch.isalpha():    # 피연산자
        print(ch, end='')
    elif ch == '(':
        operator.append(ch)
    elif ch == '+' or ch == '-':
        while operator and operator[-1] != '(': # 나보다 우선 순위 낮은 연산자 나올 때까지 pop
            print(operator.pop(), end='')
        operator.append(ch)
    elif ch == '*' or ch == '/':
        while operator and (operator[-1] == '*' or operator[-1] == '/'): # 나와 우선 순위가 같은 연산자는 모두 pop
            print(operator.pop(), end='')
        operator.append(ch)
    elif ch == ')':
        while operator[-1] != '(':
           print(operator.pop(), end='')
        operator.pop()  # '(' pop
if operator:    # operator 배열에 남은 연산자들 처리
    print(''.join(reversed(operator)))