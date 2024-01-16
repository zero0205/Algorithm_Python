def bs(target, lst):
    s, e = 0, n-1
    while s <= e:
        mid = (s+e)//2
        if lst[mid] == target:
            return 1
        if lst[mid] < target:
            s = mid+1
        else:
            e = mid-1
    return 0


for _ in range(int(input())):
    n = int(input())
    d1 = list(map(int, input().split()))
    m = int(input())
    d2 = list(map(int, input().split()))

    d1.sort()

    for num in d2:
        print(bs(num, d1))
