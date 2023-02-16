import sys
from collections import deque

stack = deque([])

def solution(cmd):
    if len(cmd) > 5:        # push
        stack.append(int(cmd.split()[1]))
    elif cmd == "pop":      # pop
        print(stack.popleft()) if stack else print(-1)
    elif cmd == "size":     # size
        print(len(stack))
    elif cmd == "empty":    # empty
        print(0) if stack else print(1)
    elif cmd == "front":    # front
        print(stack[0]) if stack else print(-1)
    elif cmd == "back":     # back
        print(stack[-1]) if stack else print(-1)
            
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    solution(cmd)
    
    
#############################################
# import sys

# stack = []

# def solution(cmd):
#     if len(cmd) > 5:        # push
#         stack.append(int(cmd.split()[1]))
#     elif cmd == "pop":      # pop
#         print(stack.pop(0)) if stack else print(-1)
#     elif cmd == "size":     # size
#         print(len(stack))
#     elif cmd == "empty":    # empty
#         print(0) if stack else print(1)
#     elif cmd == "front":    # front
#         print(stack[0]) if stack else print(-1)
#     elif cmd == "back":     # back
#         print(stack[-1]) if stack else print(-1)
            
# n = int(sys.stdin.readline())
# for _ in range(n):
#     cmd = sys.stdin.readline().strip()
#     solution(cmd)