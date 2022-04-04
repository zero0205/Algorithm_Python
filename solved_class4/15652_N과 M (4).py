# https://www.acmicpc.net/problem/15652

from itertools import combinations_with_replacement

n, m = map(int, input().split())

lst = list(combinations_with_replacement(range(1, n + 1), m))

for el in lst:
    for e in el:
        print(e, end=" ")
    print()