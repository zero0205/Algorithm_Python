import sys

n = int(sys.stdin.readline())
stack = []
cnt = 1
ans = []

for _ in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num:
        stack.append(cnt)
        ans.append("+")
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
       print("NO")
       exit()
            
for el in ans:
    print(el)