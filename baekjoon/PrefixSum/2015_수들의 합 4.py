from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
ps_dict = defaultdict(int)
tmp = 0
for a in arr:
    tmp += a
    if tmp == k:    # 처음부터 이제까지 누적합이 k라면
        ans += 1
    
    ans += ps_dict[tmp-k]   # 합이 k를 만들 수 있는 구간합이 있다면
    ps_dict[tmp] += 1
print(ans)