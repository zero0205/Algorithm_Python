input_data = input()

stack = []
ans = 0

for i in range(len(input_data)):
    if input_data[i] == '(':
        stack.append('(')
    else:
        if input_data[i-1] == '(':  # 레이저인 경우
            stack.pop()
            ans += len(stack)
        else:                       # 쇠막대기의 오른쪽 끝
            stack.pop()
            ans += 1
print(ans)