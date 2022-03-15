# https://www.acmicpc.net/problem/11659
import sys

n, m = map(int, input().split())
num_arr = list(map(int, input().split()))

# 누적합 구하기
sum_arr = []
sum_arr.append(num_arr[0])
for i in range(1, n):
    sum_arr.append(sum_arr[i-1] + num_arr[i])
    
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a < 2:
        print(sum_arr[b-1])
    else:
        print(sum_arr[b-1]-sum_arr[a-2])