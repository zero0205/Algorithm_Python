str = input()

stack = []
acc = [[0]*2 for _ in range(len(str)+1)]
for i in range(len(str)):
    if str[i] == '(':
        acc[i+1][0] = acc[i][0] + 1
        acc[i+1][1] = acc[i][1]
        stack.append(i+1)
    else:
        acc[i+1][0] = acc[i][0]
        acc[i+1][1] = acc[i][1] + 1
        if stack:
            stack.pop()
        else:
            print(acc[i+1][1])
            exit()

if stack:   # '(' 괄호가 더 많음
    print(acc[-1][0]-acc[stack[-1]][0]+1)
else:
    print(0)
