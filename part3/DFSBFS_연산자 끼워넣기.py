# https://www.acmicpc.net/problem/14888

# # 수의 개수 입력받기
# n = int(input())
# # 수 입력받기
# num = list(map(int, input().split()))
# # 연산 개수 입력받기(+, -, *, / 순서)
# op = list(map(int, input().split()))

# max_num = int(1e9)* (-1)
# min_num = int(1e9) 

# def copy_sub_arr(arr, idx):
#     new_arr = [0, 0, 0 ,0]
#     for i in range(len(arr)):
#         new_arr[i] = arr[i]
#     new_arr[idx] -= 1
#     return new_arr

# def dfs(num, op, res):
#     global max_num, min_num
#     # num 다 썼으면 리턴
#     if len(num) == 0:
#         if res < min_num:
#             min_num = res
#         if res > max_num:
#             max_num = res
#         return

#     for i in range(4):
#         if op[i] == 0:  # 연산 다 소모함
#             continue
#         if i == 0:  # 덧셈
#             res += num[0]
#             new_op = copy_sub_arr(op, 0)
#         elif i == 1:    # 뺄셈
#             res -= num[0]
#             new_op = copy_sub_arr(op, 1)
#         elif i == 2:    # 곱셈
#             res *= num[0]   
#             new_op = copy_sub_arr(op, 2)
#         elif i == 3:    # 나눗셈
#             res = res // num[0]
#             new_op = copy_sub_arr(op, 3)
#         dfs(num[1:], new_op, res)

# res = num[0]
# dfs(num[1:], op, res)
# print(max_num)
# print(min_num)

###############################
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최댓값과 최솟값 초기화
min_value = 1e9
max_value = -1e9

# DFS 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))  # 나눌 때는 나머지를 제거
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)