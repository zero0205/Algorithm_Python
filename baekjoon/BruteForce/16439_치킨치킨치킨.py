from itertools import combinations

n, m = map(int, input().split())
preference = []
for i in range(n):
    preference.append(list(map(int, input().split())))
    
def get_satisfaction(memeber, orders):
    max_pref = 0
    for i in [preference[memeber][j] for j in orders]:
        max_pref = max(max_pref, i)
    return max_pref

ans = 0
for orders in list(combinations(range(m), 3)):
    total = 0
    for i in range(n):
        total += get_satisfaction(i, orders)
    ans = max(ans, total)
print(ans)