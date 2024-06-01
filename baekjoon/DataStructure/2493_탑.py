n = int(input())
towers = list(map(int, input().split()))

stack = []
ans = [0]*n

for i in range(n):
    while stack and stack[-1][0] <= towers[i]:
        stack.pop()
    ans[i] = (stack[-1][1]+1 if stack else 0)
    stack.append((towers[i], i))
print(*ans)
