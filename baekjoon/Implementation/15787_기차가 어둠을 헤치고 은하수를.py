# import sys
# input = sys.stdin.readline
# from collections import deque

# n, m = map(int, input().split())
# train = [deque([0] * 20) for _ in range(n)]    # 각각 20개의 좌석이 있는 n개의 기차
# for _ in range(m):
#     cmd = list(map(int, input().split()))
#     if cmd[0] == 1:
#         if train[cmd[1]-1][cmd[2]-1] == 0:
#             train[cmd[1]-1][cmd[2]-1] = 1    # 승차
#     elif cmd[0] == 2:
#         if train[cmd[1]-1][cmd[2]-1] == 1:
#             train[cmd[1]-1][cmd[2]-1] = 0   # 하차
#     elif cmd[0] == 3:
#         train[cmd[1]-1].rotate(1)
#         train[cmd[1]-1][0] = 0
#     else:
#         train[cmd[1]-1].rotate(-1)
#         train[cmd[1]-1][19] = 0
            
# lst = set()
# for i in range(n):
#     if tuple(train[i]) in lst:    # 이미 목록에 존재하는 기록
#         continue
#     lst.add(tuple(train[i]))
    
# print(len(lst))

###### 비트마스킹 #######
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [0] * (n+1)
for _ in range(m):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        train[cmd[1]] |= (1 << (cmd[2]-1))
    elif cmd[0] == 2:
        train[cmd[1]] &= ~(1 << (cmd[2]-1))
    elif cmd[0] == 3:
        train[cmd[1]] = train[cmd[1]] << 1
        train[cmd[1]] &= ~(1 << 20)
    else:
        train[cmd[1]] = train[cmd[1]] >> 1

print(len(set(train[1:])))