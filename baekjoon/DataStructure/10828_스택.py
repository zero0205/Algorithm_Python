import sys

stack = []

def solution(cmd):
    if len(cmd) > 5:        # push
        stack.append(int(cmd.split()[1]))
    elif cmd == "pop":      # pop
        print(stack.pop()) if stack else print(-1)
    elif cmd == "size":     # size
        print(len(stack))
    elif cmd == "empty":    # empty
        print(0) if stack else print(1)
    elif cmd == "top":      # top
        print(stack[-1]) if stack else print(-1)
            
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    solution(cmd)