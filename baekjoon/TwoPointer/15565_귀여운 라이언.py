import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dolls = list(map(int, input().split()))

l = 0
answer = n+1
lion = 0
for r in range(n):
    if dolls[r] == 1:
        lion += 1
    while lion >= k:
        if lion == k and dolls[l] == 1:
            break
        if dolls[l] == 1:
            lion -= 1
        l += 1
    if lion == k:
        answer = min(answer, r-l+1)

print(answer if answer != n+1 else -1)
