import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = 0
for i in range(n):
    l, r = 0, n-1
    while l < r:
        if l == i:
            l += 1
        if r == i:
            r -= 1
        if l >= r:
            break
        if arr[l]+arr[r] == arr[i]:
            ans += 1
            break
        elif arr[l]+arr[r] < arr[i]:
            l += 1
        else:
            r -= 1
print(ans)
