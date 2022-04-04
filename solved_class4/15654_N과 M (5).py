# https://www.acmicpc.net/problem/15654

from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for el in list(permutations(sorted(arr), m)):
    for e in el:
        print(e, end=" ")
    print()