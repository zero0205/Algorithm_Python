# https://www.acmicpc.net/problem/18870/

from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

arr_cpy = set(arr)
arr_cpy = list(arr_cpy)
arr_cpy.sort()

for el in arr:
    print(bisect_left(arr_cpy, el),end=' ')