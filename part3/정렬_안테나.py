# n 입력받기
n = int(input())
# 집 위치들 입력받기
arr = list(map(int, input().split()))
arr.sort()

# min = int(1e9)
# min_loc = int(1e9)
# for i in arr:
#     sum = 0
#     for j in arr:
#         sum += abs(i-j)
#         # for문 도는 중에 이미 최소값보다 커져버리면 더이상 진행 X
#         if sum > min:
#             break
#     if sum < min:
#         min = sum
#         min_loc = i

# print(min_loc)

print(arr[(len(arr) - 1)//2])