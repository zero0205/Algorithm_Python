from itertools import combinations

n = input()
max_v = -int(1e9)
min_v = int(1e9)
def odd_love(num, odd_cnt):
    global min_v, max_v
    # 홀수 개수 세기
    for i in range(len(num)):
        if int(num[i]) % 2 == 1:
           odd_cnt += 1 
    # 1자리수
    if len(num) == 1:
        max_v = max(max_v, odd_cnt)
        min_v = min(min_v, odd_cnt)
        return 
    # 2자리수
    elif len(num) == 2:
        odd_love(str(int(num[0])+int(num[1])), odd_cnt)
    # 수가 3자리 이상
    else:
        for a, b in combinations(range(1, len(num)), 2):
            s = sum(map(int, [num[:a], num[a:b], num[b:]]))
            odd_love(str(s), odd_cnt)
        
odd_love(n, 0)
print(min_v, max_v)