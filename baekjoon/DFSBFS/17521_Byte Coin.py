import sys
sys.setrecursionlimit(10**6)

n, w = map(int, input().split())
s = [int(input()) for _ in range(n)]

ans = -1


def dfs(date, coin, money):
    global ans
    if date == n:
        if ans < money:
            ans = money
        return
    # 매수 (갖고 있는 돈으로 최대치 매수)
    dfs(date+1, coin+money//s[date], money % s[date])
    # 매도 (갖고 있는 코인 모두 매도)
    dfs(date+1, 0, money+coin*s[date])


dfs(0, 0, w)
print(ans)
