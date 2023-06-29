import sys
input = sys.stdin.readline

n, k = map(int, input().split())
test = list(map(int, input().split()))
acc = [0] # 누적합
for i in range(n):
    acc.append(acc[i]+test[i])

def possible(mid):
    cnt = 0
    prev = 0
    for i in range(len(acc)):
        if (acc[i] - acc[prev]) >= mid:
            prev = i
            cnt += 1
    if cnt >= k:
        return True
    else:
        return False

# 현수가 받을 수 있는 최대의 점수 구하기
start, end = 0, 20 * int(1e5)
ans = 0
while start <= end:
    mid = (start + end) // 2
    if possible(mid):
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)        