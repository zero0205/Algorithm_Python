# https://www.acmicpc.net/problem/9461
# import math

# p = [0, 1 ,1 ,1 ,2 ,2 ,3 ,4 ,5 ,7, 9]   # 0~10까지
# term = 5
# for i in range(11, 101):
#     p.append(p[i - math.floor(term)] + p[i - 1])
#     term += 0.5

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     print(p[n])
    
###############################

p = [0, 1 ,1 ,1 ,2 ,2 ,3 ,4 ,5 ,7, 9]   # 0~10까지

for i in range(11, 101):
    p.append(p[i - 3] + p[i - 2])

t = int(input())
for _ in range(t):
    n = int(input())
    print(p[n])