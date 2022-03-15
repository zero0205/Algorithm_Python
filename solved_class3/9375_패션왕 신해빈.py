# https://www.acmicpc.net/problem/9375

from itertools import combinations
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dict = {}
    # 의상 이름, 종류 입력받기
    for _ in range(n):
        name, ty = input().split()
        if ty in dict:
            dict[ty] += 1
        else:
            dict[ty] = 1
            
    ans = 1
    for num in dict.values():
        ans *= (num + 1)
        
    print(ans - 1)