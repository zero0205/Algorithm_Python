# https://www.acmicpc.net/problem/11723

#### 이거 안되는 풀이 ######
# import sys
# input = sys.stdin.readline

# # 연산의 개수 m 입력받기
# m = int(input())
# # 비어있는 공집합 리스트 S
# S = [False] * 21
# # 연산들 입력받기
# for _ in range(m):
#     cmd= input()
#     if cmd[:3] == "all":
#         for s in S:
#             s = True
#         continue
#     elif cmd[:5] == "empty":
#         for s in S:
#             s = False
#         continue
#     else:
#         cmd, num = cmd.split()
#         num = int(num)
    
#         if cmd == "add":
#             S[num] = True
#         elif cmd == "remove":
#             S[num] = False
#         elif cmd == "check":
#             if S[num]:
#                 print(1)
#             else:
#                 print(0)
#         elif cmd == "toggle":
#             S[num] = False if S[num] else True

############# 비트마스크 ################
import sys

# 연산의 개수 m 입력받기
m = int(sys.stdin.readline())

bit = 0 # 비트마스크용

# 연산들 입력받기
for _ in range(m):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 1:
        if cmd[0] == "all":
            bit = (1 << 20) - 1
        else:   # empty
            bit = 0
    else:
        cmd, num = cmd[0], cmd[1] 
        num = int(num)
        if cmd == "add":
            bit |= (1 << (num - 1))
        elif cmd == "remove":
            bit &= ~(1 << (num - 1))
        elif cmd == "check":
            print(1) if (bit & (1 << (num - 1)) > 0) else print(0)
        elif cmd == "toggle":
            bit = bit ^ (1 << (num - 1))
############# set ################# 
# import sys

# # 연산의 개수 m 입력받기
# m = int(sys.stdin.readline())
# S = set()   # 집합
# # 연산들 입력받기
# for _ in range(m):
#     cmd = sys.stdin.readline().split()
#     if len(cmd) == 1:
#         if cmd[0] == "all":
#             S = set([i for i in range(1, 21)])
#         else:   # empty
#             S = set()
#     else:
#         cmd, num = cmd[0], cmd[1] 
#         num = int(num)
#         if cmd == "add":
#             S.add(num)
#         elif cmd == "remove":
#             S.discard(num)
#         elif cmd == "check":
#             print(1 if (num in S) else 0)
#         elif cmd == "toggle":
#             S.discard(num) if (num in S) else S.add(num)