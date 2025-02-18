import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))


def count_section(target):
    max_value = min_value = arr[0]
    cnt = 1
    for i in range(1, n):
        if max_value < arr[i]:
            max_value = arr[i]
        if min_value > arr[i]:
            min_value = arr[i]
        if max_value - min_value > target:
            cnt += 1
            max_value = min_value = arr[i]
    return cnt


def binary_search(sections):
    l, r = 0, 10000
    answer = 0
    while l <= r:
        mid = (r+l)//2
        if count_section(mid) <= sections:
            r = mid-1
            answer = mid
        else:
            l = mid+1
    return answer


print(binary_search(m))
