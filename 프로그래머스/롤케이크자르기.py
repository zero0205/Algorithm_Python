# def solution(topping):
#     answer = 0

#     acc = [0]*(len(topping))    # 왼쪽에서부터 누적합
#     acc_reverse = [0]*(len(topping))    # 오른쪽에서부터 누적합
#     s = set()
#     s_reverse = set()
#     # 누적합 구하기
#     for i in range(len(topping)):
#         s.add(topping[i])
#         acc[i] = len(s)
#         s_reverse.add(topping[len(topping)-1-i])
#         acc_reverse[len(topping)-1-i] = len(s_reverse)

#     # 공평하게 나누는 지점들 찾기
#     for i in range(len(topping)-1):
#         if acc[i] == acc_reverse[i+1]:
#             answer += 1

#     return answer

from collections import Counter


def solution(topping):
    answer = 0
    right = Counter(topping)
    left = set()
    for i in range(len(topping)):
        left.add(topping[i])
        right[topping[i]] -= 1
        if right[topping[i]] == 0:
            right.pop(topping[i])
        if len(left) == len(right):
            answer += 1
        elif len(left) > len(right):
            break
    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
# 2
print(solution([1, 2, 3, 1, 4]))
# 0
