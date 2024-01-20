from collections import defaultdict
import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    scores = defaultdict(int)   # 각 선수들의 포인트 저장
    for _ in range(n):
        for j in map(int, input().split()):
            scores[j] += 1
    # scores에서 포인트만 뽑아내서 내림차순 정렬
    only_score = sorted(scores.values(), reverse=True)
    second = []  # 2등인 선수들
    for player in scores.keys():
        if scores[player] == only_score[1]:
            second.append(player)
    print(*sorted(second))  # 2등 선수들 오름차순 출력
