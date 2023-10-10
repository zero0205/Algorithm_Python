weight_num = int(input())
weight = list(map(int, input().split()))
marble_num = int(input())
marble = list(map(int, input().split()))

# i번째 추까지 사용해서 j 무게 만들 수 있는지 여부
dp = [[False] * 15_001 for _ in range(weight_num+1)]


def dfs(left, right, idx):
    diff = abs(left-right)
    if dp[idx][diff]:
        return
    dp[idx][diff] = True
    if idx > weight_num-1:
        return
    # 왼쪽 올림
    dfs(left+weight[idx], right, idx+1)
    # 오른쪽 올림
    dfs(left, right+weight[idx], idx+1)
    # 안 올림
    dfs(left, right, idx+1)


dfs(0, 0, 0)
for m in marble:
    if m > 15_000:
        print('N')
    else:
        print('Y' if dp[weight_num][m] else 'N', end=" ")
