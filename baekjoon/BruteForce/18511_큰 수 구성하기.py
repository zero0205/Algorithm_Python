from itertools import product

n, k = map(int, input().split())
k_arr = list(input().split())

ans = 0
for i in range(len(str(n)), len(str(n))-2, -1):
    for comb in product(k_arr, repeat=i):
        num = int(''.join(comb))
        if num <= n:
            ans = max(ans, num)
print(ans)