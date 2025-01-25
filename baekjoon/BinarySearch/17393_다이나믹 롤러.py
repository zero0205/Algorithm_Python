n = int(input())
inks = list(map(int, input().split()))
viscosities = list(map(int, input().split()))


def binary_search(start, target):
    l, r = start, n-1
    res = n-1
    while l <= r:
        mid = (l+r)//2
        if viscosities[mid] <= target:
            res = mid
            l = mid+1
        else:
            r = mid-1
    return res


ans = []
for i in range(n):
    ans.append(binary_search(i, inks[i])-i)

print(*ans)
