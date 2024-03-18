for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    highest = -1
    ans = 0
    for i in range(n-1, -1, -1):
        if highest < lst[i]:
            highest = lst[i]
        else:
            ans += (highest-lst[i])
    print(ans)
