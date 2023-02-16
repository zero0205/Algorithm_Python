import sys
input = sys.stdin.readline

tip = []
for _ in range(int(input())):
    tip.append(int(input()))

tip.sort(reverse=True)

ans = 0
for i in range(1, len(tip) + 1):
    tmp = tip[i-1] - (i - 1)
    if tmp > 0:
        ans += tmp
        
print(ans)