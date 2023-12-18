def chk(w):
    stack = []
    for i in range(len(w)):
        if not stack or stack[-1] != w[i]:
            stack.append(w[i])
        else:
            stack.pop()
    return False if stack else True


n = int(input())
ans = 0
for _ in range(n):
    word = input()
    if chk(word):
        ans += 1
print(ans)
