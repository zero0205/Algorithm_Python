from itertools import combinations

n = int(input())
all = set([i for i in range(n)])
ability = []
for _ in range(n):
    ability.append(list(map(int, input().split())))
    
def get_ability(team):
    if len(team) == 1:
        return 0
    res = 0
    for m1, m2 in combinations(team, 2):
        res += (ability[m1][m2] + ability[m2][m1])
    return res

ans = int(1e9)
for i in range(1, n//2+1):
    for start in combinations(all, i):
        link = all - set(start)
        diff = abs(get_ability(start) - get_ability(link))
        ans = min(ans, diff)
        
print(ans)