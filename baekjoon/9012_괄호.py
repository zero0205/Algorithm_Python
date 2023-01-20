def vps(input_str):
    stack = []
    for i in input_str:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()  
            else: 
                return "NO"
    # 스택이 남아있으면 VPS가 아님
    return "NO" if stack else "YES"

t = int(input())
for _ in range(t):
    input_str = input()
    print(vps(input_str))