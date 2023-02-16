import sys

stack = []
cnt = 1
ans = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    while stack and stack[-1] > num:   # stack의 top에 있는 숫자가 지금 들어온 숫자보다 크다면 모두 pop
        stack.pop()
        ans.append('-')
    while cnt <= num:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
    if stack and stack[-1] == num:
        stack.pop() # 본인 pop
        ans.append('-')
    else:   # 이 숫자가 스택에 없음
        print("NO")
        exit()
    
for i in ans:
    print(i)