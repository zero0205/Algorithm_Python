n = int(input())
weights = list(map(int, input().split()))

ans = 0


def bt(w, total):
    global ans
    if len(w) < 3:
        ans = max(ans, total)
        return
    for i in range(1, len(w)-1):
        bt(w[:i]+w[i+1:], total+(w[i-1]*w[i+1]))


bt(weights, 0)
print(ans)
