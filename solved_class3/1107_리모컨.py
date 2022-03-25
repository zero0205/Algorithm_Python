# https://www.acmicpc.net/problem/1107

# 이동하려는 채널
n = int(input())
# 고장난 버튼의 개수
m = int(input())
# 고장난 버튼들 (m개)
if m == 0:
    broken = []
else:
    broken = list(input().split())

ans = abs(n - 100)

for num in range(999999):
    num_str = str(num)
    for i in num_str:
        if i in broken: # 고장난 버튼 필요한 경우
            break
    else:
        ans = min(ans, len(num_str) + abs(n - num))

print(ans)