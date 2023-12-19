# from itertools import combinations

# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))

# s = set()
# for comb in combinations(arr, m):
#     if comb not in s:
#         s.add(comb)
#         print(*comb)

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []


def bt(idx, selected):
    if len(selected) == m:  # 선택된 숫자가 m개
        if selected not in s:   # 아직 출력된 적 없는 수열이라면 출력
            print(*selected)
            s.append(selected)
        return
    if idx+1 < n:
        bt(idx+1, sorted(selected+[arr[idx+1]]))    # idx+1번째 원소 포함 O
        bt(idx+1, selected)                         # idx+1번째 원소 포함 X


bt(-1, [])
