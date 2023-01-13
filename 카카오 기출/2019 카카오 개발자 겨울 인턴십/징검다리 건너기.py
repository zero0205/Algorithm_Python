# def solution(stones, k):
#     answer = 0
#     arr = []
#     for idx in range(len(stones)):
#         # 이전에 밟을 수 있는 돌 인덱스, 다음에 밟을 수 있는 돌 인덱스, 디딤돌 숫자
#         arr.append([idx - 1, idx + 1, stones[idx]])  
#     flag = False
#     while flag == False:
#         # stones 배열 전체 돌며 밟을 수 있는 디딤돌 숫자 - 1
#         for i in range(len(arr) + 1):
#             if arr[i][2] >= 1:  # 아직 밟을 수 있는 돌이라면
#                 arr[i][2] -= 1
#                 if arr[i][2] == 0 and arr[i][1] < len(stones) - 1:  # 이번에 밟을 수 있는 횟수 모두 소모
#                     if arr[i][1] - arr[arr[i][0]][1] >= k:  # 다음 애들은 못 건널거임
#                         flag = True
#                         break
#                     else:
#                         arr[arr[i][0]][1] = arr[i][1]
#     return answer
###################
def solution(stones, k):
    left = 1
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for s in stones:
            if s - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left

# 테스트 케이스
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))