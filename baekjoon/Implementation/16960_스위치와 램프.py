from collections import defaultdict

n, m = map(int, input().split())
lamp_count = defaultdict(int)
switch_lamp = []

for _ in range(n):
    num, *arr = list(map(int, input().split()))
    switch_lamp.append(arr)
    for a in arr:
        lamp_count[a] += 1

for i in range(n):
    possible = True
    for lamp in switch_lamp[i]:
        if lamp_count[lamp] == 1:
            possible = False
            break
    if possible:
        print(1)
        exit()
print(0)
