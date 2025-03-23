from itertools import combinations

n = int(input())
dice = list(map(int, input().split()))

one_min = min(dice)

two_min = int(1e9)
for comb in combinations(range(6), 2):
    if sum(comb) == 5:
        continue
    total = dice[comb[0]]+dice[comb[1]]
    if total < two_min:
        two_min = total

three_min = int(1e9)
for comb in combinations(range(6), 3):
    if comb[0]+comb[1] == 5 or comb[1]+comb[2] == 5 or comb[0]+comb[2] == 5:
        continue
    total = dice[comb[0]]+dice[comb[1]]+dice[comb[2]]
    if total < three_min:
        three_min = total

answer = 0
if n == 1:
    answer = sum(dice)-max(dice)
elif n == 2:
    answer += two_min*4
    answer += three_min*4
else:
    answer += one_min*((n-2)**2 + (n-1)*(n-2)*4)
    answer += two_min*((n-2)*4+(n-1)*4)
    answer += three_min*4

print(answer)
