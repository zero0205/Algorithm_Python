from itertools import combinations


def bt(idx):
    global ans, match_results
    if idx == 15:
        ans = 1
        for nation in match_results:
            if nation.count(0) != 3:
                ans = 0
                break
        return
    home, away = matchs[idx]
    for h, w in [(0, 2), (1, 1), (2, 0)]:   # home 이김, 비김, home 짐
        if match_results[home][h] > 0 and match_results[away][w] > 0:
            match_results[home][h] -= 1
            match_results[away][w] -= 1
            bt(idx+1)
            match_results[home][h] += 1
            match_results[away][w] += 1


answer = []
matchs = list(combinations(range(6), 2))
for i in range(4):
    line = list(map(int, input().split()))
    match_results = [line[i*3:i*3+3] for i in range(6)]
    ans = 0
    bt(0)
    answer.append(ans)

print(*answer)
