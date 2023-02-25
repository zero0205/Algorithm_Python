from itertools import combinations

def check(comb, ban):
    c_ptr = 0
    b_ptr = 0
    while True:
        if b_ptr == len(ban):
            return False
        if c_ptr == len(comb):
            return True
        if comb[c_ptr] == ban[b_ptr]:   # 부작용 일으키는 성분 포함
            b_ptr += 1
        c_ptr += 1

def solution(n, bans):
    answer = 0
    for i in range(1, n+1):
        # i개의 약으로 만들 수 있는 조합
        comb = combinations(range(1,n+1), i)
        for c in comb:
            flag = True
            for b in bans:
                b = list(map(int, b.split()))
                if not flag:
                    break
                if not check(c, b): # 만들 수 없는 조합
                    flag = False
                    break
            if flag:
                answer += 1
    return answer