from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
ans = deque()
for i in range(n):
    if cards[n-1-i] == 1:   # 제일 위의 카드 1장 내려놓음
        ans.appendleft(i+1)
    elif cards[n-1-i] == 2:     # 위에서 두번째 카드 내려놓음(카드 2장 이상일 때 사용 가능)
        tmp = ans.popleft()
        ans.appendleft(i+1)
        ans.appendleft(tmp)
    else:       # 제일 밑의 카드 내려놓음(카드 2장 이상일 때 사용 가능)
        ans.append(i+1)
print(*ans)
