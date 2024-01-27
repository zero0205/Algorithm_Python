def bs(arr, target):
    s, e = 0, len(arr)-1
    res = -1
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == target:
            res = mid
            break
        elif arr[mid] < target:
            res = mid
            s = mid+1
        else:
            e = mid-1
    return res


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))
    sum_c = 0
    for i in range(n):
        near = bs(b, a[i])
        if near < m-1 and abs(b[near+1]-a[i]) < abs(b[near]-a[i]):
            near += 1
        sum_c += b[near]
    print(sum_c)
