from collections import deque
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
dp = [-1]*(n+1)     # dp[i]는 1번에서 i번까지 가는 길에 가장 처음 마주치는 점유된 땅 번호
for i in range(q):
    want = int(input())
    if dp[want] == -1:  # 가는 길에 이미 점유된 땅이 없음
        # 이 땅 아래로는 다 이 땅을 지나야만 한다고 표시
        q = deque([want])
        while q:
            now = q.popleft()
            dp[now] = want
            for nx in [now*2, now*2+1]:
                if nx <= n:
                    q.append(nx)
        print(0)
    else:   # 가는 길에 점유된 땅이 있음
        print(dp[want])
