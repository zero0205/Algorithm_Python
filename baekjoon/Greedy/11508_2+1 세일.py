# import sys
# input = sys.stdin.readline

# n = int(input())
# cost = []
# for _ in range(n):
#     cost.append(int(input()))

# cost.sort(reverse=True)

# package = []
# for i in range(0, n, 3):
#     package.append(cost[i:i+3])

# ans = 0
# for p in package:
#     if len(p) < 3:
#         ans += sum(p)
#     else:
#         ans += sum(p) - min(p)
        
# print(ans)

######################################
import sys
input = sys.stdin.readline

n = int(input())
cost = []
for _ in range(n):
    cost.append(int(input()))

cost.sort(reverse=True)

ans = 0
for i in range(0, n, 3):
    if i < n - 1:
        ans += cost[i] + cost[i + 1]
    else:   # 마지막에 물건이 1개만 남는 경우
        ans += cost[i]
        
print(ans)

######### 다른 풀이 ###########
# n=int(input())
# c=[]
# for i in range(n):
#   c.append(int(input()))
# c.sort(reverse=True)

# result=0
# for i in range(2,len(c),3):
#   result+=c[i]

# print(sum(c)-result)