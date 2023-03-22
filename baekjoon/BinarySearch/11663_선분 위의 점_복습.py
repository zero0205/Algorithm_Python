import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dot = sorted(list(map(int, input().split())))

def bs_left(target):
    start, end = 0, len(dot)-1
    while start <= end:
        mid = (start+end) // 2
        if dot[mid] == target:
            return mid
        if dot[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return end

def bs_right(target):
    start, end = 0, len(dot)-1
    while start <= end:
        mid = (start+end) // 2
        if dot[mid] == target:
            return mid
        if dot[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for _ in range(m):
    left, right = map(int, input().split())
    print(bs_left(right) - bs_right(left) + 1)
####################################################
# from bisect import bisect_left, bisect_right
# n, m = map(int, input().split())
# dot = sorted(list(map(int, input().split())))

# for _ in range(m):
#     left, right = map(int, input().split())

#     print(bisect_right(dot, right) - bisect_left(dot, left))