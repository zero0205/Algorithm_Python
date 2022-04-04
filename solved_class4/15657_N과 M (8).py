# https://www.acmicpc.net/problem/15657

from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for el in list(combinations_with_replacement(sorted(arr), m)):
    for e in el:
        print(e, end=" ")
    print()