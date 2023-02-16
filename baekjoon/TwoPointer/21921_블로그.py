################# 시간 초과 ###################
# import sys
# input = sys.stdin.readline

# n, x = map(int, input().split())
# visitor = list(map(int, input().split()))

# max_visitor = 0
# cnt = 0

# for i in range(n-x+1):
#     total = sum(visitor[i:i+x])
#     if max_visitor < total:
#         max_visitor = total
#         cnt = 1
#     elif max_visitor == total:
#         cnt += 1    
        
# if max_visitor == 0:
#     print("SAD")
# else:
#     print(max_visitor)
#     print(cnt)
##############################################
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitor = list(map(int, input().split()))

if max(visitor) == 0:
    print("SAD")
    exit()

# 누적합 구하기
acc = [0]
for i in range(n):
    acc.append(acc[i] + visitor[i])

max_visitor = acc[x] - acc[0]
cnt = 1

for i in range(1, n-x+1):
    total = acc[i+x]-acc[i]
    if max_visitor < total:
        max_visitor = total
        cnt = 1
    elif max_visitor == total:
        cnt += 1    

print(max_visitor)
print(cnt)