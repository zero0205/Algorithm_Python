from itertools import permutations

n = int(input())

set_num = set([tuple(map(str, comb))
              for comb in permutations(range(1, 10), 3)])   # 가능한 숫자 집합

for _ in range(n):
    num, strike, ball = map(int, input().split())
    new_set = set()
    for arr in set_num:
        s, b = 0, 0
        for j in range(3):  # 스트라이크 & 볼 개수 세기
            result = str(num).find(arr[j])
            if result == j:
                s += 1
            elif result != j and result >= 0:
                b += 1
        if strike == s and ball == b:
            new_set.add(arr)
    set_num = set_num & new_set

print(len(set_num))
