################ 시간 초과 ##################
# from collections import defaultdict

# for _ in range(int(input())):
#     w = input()
#     k = int(input())
    
#     # 3번
#     start, end = 0, 0
#     count = defaultdict(int)
#     min_len = 10001
    
#     while end < len(w):
#         count[w[end]] += 1
#         if count[w[end]] == k:  # 어떤 문자를 정확히 K개 포함
#             while count[w[end]] == k and w[start] != w[end]:
#                 count[w[start]] -= 1
#                 start += 1
#             min_len = min(min_len, end-start+1)
#             count[w[start]] -= 1
#             start += 1
#         end += 1
#     # 만족하는 연속 문자열이 없는 경우
#     if min_len == 10001:
#         print(-1)
#     else:
#         # 4번
#         max_len = -1
#         flag = False
#         for length in range(len(w), -1, -1):
#             if flag:
#                 break
#             for i in range(len(w)-length):
#                 if w[i] == w[i+length-1] and w[i:i+length].count(w[i]) == k:
#                     max_len = length
#                     flag = True
#                     break
#         print(min_len, max_len)
#################################################
from collections import defaultdict

def str_game(w, k):
    over_k = defaultdict(list)
    for i in range(len(w)):
        # w에 k개 이상 포함된 문자를 over_k 딕셔너리에 {문자 : 위치리스트} 형태로 저장
        if w.count(w[i]) >= k:
            over_k[w[i]].append(i)
    if len(over_k) == 0:
        return [-1]
    min_len = 10001
    max_len = 0
    for pos_list in over_k.values():
        for j in range(len(pos_list)-k+1):
            # 해당 문자를 k개만큼 포함한 문자열의 길이 : pos_list[j+k-1]-pos_list[j]+1
            min_len = min(min_len, pos_list[j+k-1]-pos_list[j]+1)
            max_len = max(max_len, pos_list[j+k-1]-pos_list[j]+1)
    return [min_len, max_len]

for _ in range(int(input())):
    w = input()
    k = int(input())
    
    print(*str_game(w, k))    