from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
result = [list(map(int, input().split())) for _ in range(n)]
ans = 0


for comb in permutations(range(1, 9), 8):
    comb = list(comb)
    order = comb[:3]+[0]+comb[3:]   # 타순

    score = 0
    idx = 0
    for i in range(n):  # 이닝
        b1, b2, b3 = 0, 0, 0    # 1, 2, 3루 주자 현황
        out = 0  # 아웃 개수
        while out < 3:
            player = order[idx]
            if result[i][player] == 0:  # 아웃
                out += 1
            elif result[i][player] == 1:    # 안타
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif result[i][player] == 2:    # 2루타
                score += (b2+b3)
                b1, b2, b3 = 0, 1, b1
            elif result[i][player] == 3:    # 3루타
                score += (b1+b2+b3)
                b1, b2, b3 = 0, 0, 1
            else:   # 홈런
                score += (b1+b2+b3+1)
                b1, b2, b3 = 0, 0, 0
            idx = (idx+1) % 9   # 다음 타자로
    if ans < score:
        ans = score
print(ans)
