import sys
input = sys.stdin.readline

n = int(input())
work = list(map(int, input().split()))
not_work = list(map(int, input().split()))

# 누적합
work_acc = [0]
not_work_acc = [0]
for i in range(n):
    work_acc.append(work_acc[i] + work[i])
    not_work_acc.append(not_work_acc[i] + not_work[i])
    
ans = 0
for i in range(1, n+1):
    # i+1일부터 남은 기간 동안 이익
    w = work_acc[-1] - work_acc[i]
    nw = not_work_acc[-1] - not_work_acc[i]
    
    ans = max(ans, work_acc[i]+nw, not_work_acc[i]+w)
    
print(ans)

##############
# 5
# 1 2 3 4 5
# 5 4 3 2 1
# 답 : 21
# 10
# 2 20 4 15 14 19 12 12 6 5
# 18 12 12 6 18 5 4 16 17 12
# 답 : 131