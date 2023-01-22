n = int(input())
postfix = input()

d = dict()
for i in range(65, 65+n):
    d[chr(i)] = int(input().strip())
    
stack = []
for c in postfix:
    if c.isalpha():
        stack.append(d[c])
    else:
        b = stack.pop()
        a = stack.pop()
        if c == "+":
            stack.append(a+b)
        elif c == "-":
            stack.append(a-b)
        elif c == "*":
            stack.append(a*b)
        elif c == "/":
            stack.append(a/b)
       
print("{:.2f}".format(stack[0]))