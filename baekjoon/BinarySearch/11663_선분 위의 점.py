import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
dot = sorted(list(map(int, input().split())))
 
def bs(arr, target, lr):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left if lr == 0 else right
 
for _ in range(m):
    start, end = map(int, input().split())
    print(bs(dot, end, 1)-bs(dot, start, 0)+1)
############ bisect 라이브러리 활용 ##############
# import sys
# input = sys.stdin.readline
# from bisect import bisect_left, bisect_right
 
# n, m = map(int, input().split())
# dot = sorted(list(map(int, input().split())))
 
# for _ in range(m):
#     start, end = map(int, input().split())
#     print(bisect_right(dot, end) - bisect_left(dot, start))