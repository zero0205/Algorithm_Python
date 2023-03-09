from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

already = set()
for comb in combinations_with_replacement(arr, m):
    if comb not in already:
        print(*comb)
        already.add(comb)