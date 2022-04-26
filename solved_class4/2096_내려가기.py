# https://www.acmicpc.net/problem/2096

import sys
input = sys.stdin.readline

n = int(input())
max_lst = [0, 0, 0]
min_lst = [0, 0, 0]
for i in range(n):
    a, b, c = map(int, input().split())
    max_a = max(max_lst[0], max_lst[1]) + a
    max_b = max(max_lst) + b
    max_c = max(max_lst[1], max_lst[2]) + c
    
    min_a = min(min_lst[0], min_lst[1]) + a
    min_b = min(min_lst) + b
    min_c = min(min_lst[1], min_lst[2]) + c
    
    max_lst = [max_a, max_b, max_c]
    min_lst = [min_a, min_b, min_c]

print(max(max_lst), min(min_lst))