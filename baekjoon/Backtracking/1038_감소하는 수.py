n = int(input())

dec = set()


def bt(num):
    dec.add(int(num))
    for i in range(9, -1, -1):
        if i > int(num[0]):
            new_num = str(i) + num
            bt(new_num)
        else:
            break


for i in range(10):
    bt(str(i))

if n >= len(dec):
    print(-1)
else:
    print(sorted(list(dec))[n])
################ 조합 이용 ######################
# from itertools import combinations

# n = int(input())
# dec = set()
# for length in range(1, 11):
#     for comb in combinations(range(10), length):
#         comb = sorted(list(comb))
#         num = 0
#         for j in range(0, length):
#             num += comb[j] * (10**j)
#         dec.add(num)
# if n >= len(dec):
#     print(-1)
# else:
#     print(sorted(list(dec))[n])
