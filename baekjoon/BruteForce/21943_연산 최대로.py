from itertools import combinations

n = int(input())
x = list(map(int, input().split()))
plus, mul = map(int, input().split())

ans = 0


def dfs(picked_cnt, remain_x, total):
    global ans
    if picked_cnt == 1:  # 마지막 덩어리
        ans = max(ans, total*sum(remain_x))
        return
    # 하나의 덩어리 고르기
    for i in range(1, len(remain_x)-picked_cnt+2):
        for comb in combinations(range(len(remain_x)), i):
            new_remain_x = []
            tmp = 0
            for i in range(len(remain_x)):
                if i in comb:
                    tmp += remain_x[i]
                else:
                    new_remain_x.append(remain_x[i])
            dfs(picked_cnt-1, new_remain_x, total*tmp)


dfs(mul+1, x, 1)
print(ans)
