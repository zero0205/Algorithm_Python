############### 최종 제출 ##################
from collections import defaultdict

def solution(k, dist, stores):
    answer = defaultdict(int)
    prev = -1
    for i in range(dist):
        if k > 0:
            k -= 1
            continue
        while prev < len(stores)-1:
            if stores[prev+1][0] > i:
                break
            prev += 1
        while prev >= 0:
            if stores[prev][1] > 0:
                break
            prev -= 1
        stores[prev][1] -= 1
        answer[stores[prev][0]] += 1
        k -= 1
    answer = [[k, v] for k, v in answer.items()]
    return sorted(answer)

###################################################
# from collections import defaultdict

# def solution(k, dist, stores):
#     answer = defaultdict(int)
#     # 앞쪽에서 최대한 적게 구매
#     now_pos = 0
#     prev = -1   # 이전 상점 인덱스(stores 배열 인덱스)
#     while now_pos < dist:
#         if k <= 0:
#             # 이전에 있던 상점 중 가까운 상점에서 최대한 사기
#             while prev < len(stores)-1:
#                 if stores[prev+1][0] > now_pos: # 지금 거리보다 이후의 상점이면 안됨
#                     break
#                 prev += 1
#             while prev >= 0:
#                 if stores[prev][1] > 0:    # 살 수 있는 물병이 있다면
#                     break
#                 prev -= 1                  # 가까운 상점에 남은 물이 없음 -> 더 이전으로
#             # prev 위치의 상점에서 물병 1병 구매
#             stores[prev][1] -= 1 
#             answer[stores[prev][0]] += 1
#         k -= 1
#         now_pos += 1
#     answer = [[k, v] for k, v in answer.items()]
#     return sorted(answer)

############################################
# from collections import defaultdict

# def solution(k, dist, stores):
#     answer = defaultdict(int)
#     remain_bottle = [0] * dist
#     for loc, cnt in stores:
#         remain_bottle[loc] = cnt
#     # 앞쪽에서 최대한 적게 구매
#     now_pos = 0
#     while now_pos < dist:
#         if k <= 0:
#             # 이전에 있던 상점 중 가까운 상점에서 최대한 사기
#             for i in range(now_pos, -1, -1):
#                 if remain_bottle[i] > 0:
#                     remain_bottle[i] -= 1 # i 위치의 상점에서 물병 1병 구매
#                     answer[i] += 1
#                     break
#         k -= 1
#         now_pos += 1
#     answer = [[k, v] for k, v in answer.items()]
#     return sorted(answer)