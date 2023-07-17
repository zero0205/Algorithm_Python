input_data = input()

stack = []
ans = 0
tmp = 1

for idx in range(len(input_data)):
    if input_data[idx] == '(':
        stack.append('(')
        tmp *= 2
    elif input_data[idx] == '[':
        stack.append('[')
        tmp *= 3
    elif input_data[idx] == ')':
        if not stack or stack[-1] != '(':
            print(0)
            exit()
        if input_data[idx-1] == '(':
            ans += tmp
        stack.pop() 
        tmp //= 2
    elif input_data[idx] == ']':
        if not stack or stack[-1] != '[':
            print(0)
            exit()
        if input_data[idx-1] == '[':
            ans += tmp
        stack.pop() 
        tmp //= 3
     
if stack:
    print(0)
else:
    print(ans)