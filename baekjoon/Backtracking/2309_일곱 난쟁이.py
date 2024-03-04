# from itertools import combinations

# h = [int(input()) for _ in range(9)]
# for comb in combinations(h, 7):
#     if sum(comb) == 100:
#         print(*sorted(comb))
#         break

######################################
h = [int(input()) for _ in range(9)]


def bt(idx, picked):
    if len(picked) == 7:
        if sum(picked) == 100:
            print(*sorted(picked))
            exit()
    if idx >= 9:
        return
    if len(picked)+(9-idx) >= 7:
        bt(idx+1, picked+[h[idx]])
        bt(idx+1, picked)


bt(0, [])
