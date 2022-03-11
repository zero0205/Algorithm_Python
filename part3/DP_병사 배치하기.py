# # n 입력받기
# n = int(input())
# # 전투력 입력받기
# arr = list(map(int, input().split()))

# d = [0] * n
# d[n-1] = 1
# limit = arr[n-1]
# exclude_idx = n
# for i in range(n-2, 0, -1):
#     if arr[i] > limit: # 앞쪽 전투력이 뒤쪽보다 높음
#         d[i] = d[i + 1] + 1
#         limit = arr[i]
#     else:   # 열외
#         if exclude_idx == n:    # 처음으로 나온 열외인 경우
#             exclude_idx = i
#         else:   # 
#             # d[i] = 
            
############################
### 답지 ###
n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LTS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
# 열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))