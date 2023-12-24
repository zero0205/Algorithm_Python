# from itertools import combinations

# while True:
#     input_data = list(map(int, input().split()))
#     if input_data[0] == 0:
#         break
#     k = input_data[0]
#     s = input_data[1:]
#     for comb in combinations(s, 6):
#         print(*comb)
#     print()

def bt(candidate, idx, selected):
    if len(selected) == 6:  # 6개 다 뽑음
        print(*selected)
        return
    if idx >= len(candidate):
        return
    bt(candidate, idx+1, selected+[candidate[idx]])   # idx 포함
    bt(candidate, idx+1, selected)                  # idx 포함 X


while True:
    input_data = list(map(int, input().split()))
    if input_data[0] == 0:
        break
    bt(input_data[1:], 0, [])
    print()
