n = int(input())
deadlines = list(map(int, input().split()))

deadlines.sort()

l, r = 0, int(1e9)
while l <= r:
    mid = (l+r)//2

    is_possible = True
    for i in range(n):
        if deadlines[i] < mid*(i+1):
            is_possible = False
            break

    if is_possible:
        l = mid+1
    else:
        r = mid-1

print(l-1)
