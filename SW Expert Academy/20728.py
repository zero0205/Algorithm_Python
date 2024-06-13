for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))

    candy.sort()
    ans = int(1e9)
    for i in range(n-k+1):
        gap = candy[i+k-1]-candy[i]
        ans = min(ans, gap)
    print(f"#{tc} {ans}")
