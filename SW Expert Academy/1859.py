import sys
input = sys.stdin.readline

for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))

    sell = arr[-1]
    ans = 0
    for i in range(n-2, -1, -1):
        if arr[i] <= sell:
            ans += (sell-arr[i])
        else:
            sell = arr[i]
    print(f"#{tc} {ans}")
