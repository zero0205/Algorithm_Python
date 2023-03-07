n = int(input())
budget = sorted(list(map(int, input().split())))
total_budget = int(input())

def check(maximum):
    total = 0
    for b in budget:
        total += min(b, maximum)
        if total > total_budget:
            return False
    return True

if check(budget[-1]):   # 모든 요청이 배정될 수 있는지 확인
    print(budget[-1])
    exit()
    
# 이분탐색으로 상한액 찾기
ans = 0
start, end = 0, budget[-1]
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1
print(ans)