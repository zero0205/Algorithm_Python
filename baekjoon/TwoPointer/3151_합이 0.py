from bisect import bisect_left

n = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0
for left in range(n-2):
    center, right = left+1, n-1
    while center < right:
        if arr[left] + arr[center] + arr[right] == 0: # 팀 만들기 가능
            if arr[center] == arr[right]:    # center~right 다 같은 수
                ans += (right - center)
            else:
                ans += (right - bisect_left(arr, arr[right]) + 1)
            center += 1
        elif arr[left] + arr[center] + arr[right] < 0:
            center += 1
        else:
            right -= 1
print(ans)