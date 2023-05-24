import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))
ans = 0

# 누적합
acc = [honey[0]]
for i in range(1,n):
    acc.append(acc[i-1]+honey[i])
    
# 벌벌꿀
for i in range(1, n-1): # i는 벌
    total = 2*acc[-1] - honey[0] - acc[i] - honey[i]
    if total > ans:
        ans = total
# 벌꿀벌
for i in range(1, n-1): # i는 꿀
    total = (acc[i] - honey[0]) + (acc[-1] - acc[i-1] - honey[-1])
    if total > ans:
        ans = total
# 꿀벌벌
for i in range(1, n-1): # i는 벌
    total = acc[i-1] + (acc[-2] - honey[i])
    if total > ans:
        ans = total
        
print(ans)