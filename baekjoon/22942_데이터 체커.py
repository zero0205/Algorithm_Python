################# 시간 초과 #################
# import sys

# n = int(sys.stdin.readline().strip())
# circle = []
# for _ in range(n):
#     x, r = map(int, sys.stdin.readline().split())
#     for c in circle:
#         if abs(r - c[1]) <= abs(c[0] - x) <= (r + c[1]):    # 두 원이 만나는 경우
#             print("NO")
#             exit()
#     circle.append((x, r))
# print("YES")

############################################
import sys
input = sys.stdin.readline

n = int(input())
circle = []  # 원의 끝(왼쪽/오른쪽) 위치, 원이 왼쪽인지 오른쪽인지, 원의 번호
for i in range(n):
    x, r = map(int, input().split())
    left = x - r
    right = x + r
    circle.append([x-r, 0, i])    # 원의 왼쪽 끝, 왼쪽이라는 표시, 원 번호
    circle.append([x+r, 1, i])    # 원의 오른쪽 끝, 오른쪽이라는 표시, 원 번호

circle.sort()    # 원 좌표들 정렬

stack = []
prev_right = -10000000
for i in range(n * 2):
    if circle[i][1] == 0:   # 원의 왼쪽이 들어왔을 때
        if prev_right == circle[i][0]:  # 이전 원과 한 교점에서 만나는 경우
            print("NO")
            exit()
        stack.append(circle[i][2])  # 원의 번호를 스택에 append
    else:                   # 원의 오른쪽이 들어왔을 때
        if stack[-1] == circle[i][2]: # 지금 나온 원과 짝이 맞다면 다른 원 안에 잘 있는 것
            stack.pop()
            prev_right = circle[i][0]
        else:
            print("NO")    
            exit()

print("YES")    # 끝까지 안 걸리고 가면 모두 교점이 없는 것