import sys
input = sys.stdin.readline

n, atk = map(int, input().split())
rooms = []
for _ in range(n):
    # t == 1: 공격력이 a이고 생명력이 h인 몬스터
    # t == 2: 용사의 공격력을 a, 생명력을 h만큼 올려주는 포션
    t, a, h = map(int, input().split())
    rooms.append([t, a, h])

def simulate(curATK, maxHP):
    curHP = maxHP
    for t, a, h in rooms:
        # 몬스터
        if t == 1:  
            mATK = h//curATK    # 몬스터가 공격받을 수 있는 횟수
            curHP -= (mATK-1 if h%curATK == 0 else mATK) * a
            if curHP <= 0:  # 용사 사망
                return False
        # 포션
        else:       
            curATK += a
            curHP += h
            if curHP > maxHP:
                curHP = maxHP
    return True

start, end = 1, sys.maxsize
ans = 0
while start <= end:
    mid = (start + end) // 2
    if not simulate(atk, mid):
        start = mid + 1
    else:
        end = mid - 1 
        ans = mid
print(ans)