import sys
input = sys.stdin.readline

n = int(input())
l = [0] + list(map(int, input().split()))

ans = [[0, -int(1e9)] for _ in range(n+1)]

# 건물보다 왼쪽
stack = []
for i in range(1, n+1):
    while stack and l[stack[-1]] <= l[i]:   # 나보다 작은 건물 pop
        stack.pop()
    # 왼쪽에 보이는 건물 ans에 추가
    ans[i][0] += len(stack)     # 왼쪽으로 볼 수 있는 건물 개수
    if stack:
        ans[i][1] = stack[-1]   # 보이는 건물 중 가장 가까운 건물
    stack.append(i)

# 건물보다 오른쪽
stack = []
for i in range(n, 0, -1):
    while stack and l[stack[-1]] <= l[i]:   # 나보다 작은 건물 pop
        stack.pop()
    # 오른쪽에 보이는 건물 ans에 추가
    ans[i][0] += len(stack)     # 오른쪽으로 볼 수 있는 건물 개수
    if stack and stack[-1]-i < i-ans[i][1]:
        ans[i][1] = stack[-1]   # 보이는 건물 중 가장 가까운 건물
    stack.append(i)

for i in range(1, n+1):
    if ans[i][0] != 0:
        print(ans[i][0], ans[i][1])
    else:
        print(0)
