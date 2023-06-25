from itertools import combinations
from copy import deepcopy

n, m, d = map(int, input().split())
board = []
enemies = []
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        if lst[j] == 1:
            enemies.append([i, j])
# 거리 계산   
def get_dist(archer, enemy):
    return abs(archer[0]-enemy[0]) + abs(archer[1]-enemy[1])

# 공격할 적 고르기
def attack(archer, enemy_lst):
    min_dist = 100
    res = None
    for i in range(len(enemy_lst)):
        dist = get_dist(archer, enemy_lst[i])
        if dist <= d and min_dist > dist:
            min_dist = dist
            res = enemy_lst[i]
    return res

# 적 제거
def eliminate(archer_position, enemy_lst):
    res = 0
    while True:
        # 종료 조건
        if not enemy_lst:
            break
        # enemy_lst 정렬
        enemy_lst.sort(key=lambda x : x[1])
        # 궁수 공격
        eliminate_enemy = []
        for i in range(3):
            attacked_enemy = attack(archer_position[i], enemy_lst)
            if attacked_enemy:
                eliminate_enemy.append(attacked_enemy)   # 공격할 적들 저장
        for e in eliminate_enemy:   # 공격한 적들 enemy_lst 리스트에서 삭제
            if e in enemy_lst:
                enemy_lst.remove(e)
                res += 1
        # 적 이동
        remove_lst = []
        for e in enemy_lst:
            e[0] += 1
            if e[0] == n:   # 성이 있는 칸으로 이동 -> 게임에서 제외
                remove_lst.append(e)
        # 성으로 이동한 적들 제외
        for e in remove_lst:
            enemy_lst.remove(e)
    return res

ans = 0
for pos in combinations(range(m), 3):   # 궁수들 가능한 위치 조합
    archers = [[n, i] for i in pos]
    enemies_copy = deepcopy(enemies)
    ans = max(ans, eliminate(archers, enemies_copy))

print(ans)