from itertools import combinations

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)

for start in combinations(range(n), n//2):
    start = set(start)
    link = set(range(n))-start

    # 스타트팀 능력치
    start_ability = 0
    for comb in combinations(list(start), 2):
        start_ability += (ability[comb[0]][comb[1]]+ability[comb[1]][comb[0]])
    # 링크팀 능력치
    link_ability = 0
    for comb in combinations(list(link), 2):
        link_ability += (ability[comb[0]][comb[1]]+ability[comb[1]][comb[0]])
    ans = min(ans, abs(start_ability-link_ability))
print(ans)
