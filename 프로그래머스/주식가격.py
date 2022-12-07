# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)-1):
#         for j in range(i+1, len(prices)):
#             if prices[i] > prices[j]:
#                 answer[i] += 1
#                 break
#             answer[i] += 1
#     return answer

########### stack 이용 풀이 #############
def solution2(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack:
            while stack and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer


# print("1 : " + str(solution([1, 2, 3, 2, 3])))
print("2 : " + str(solution2([1, 2, 3, 2, 3])))
# [4, 3, 1, 1, 0]