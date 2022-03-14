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
        name, kind = input().split()
        if kind in dict:
            lst = dict[kind]
            lst.append(name)
            dict[kind] = lst
        else:
            dict[kind] = [name]