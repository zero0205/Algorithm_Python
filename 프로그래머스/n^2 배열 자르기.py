############ Error!!! ############
############ 시간 초과 ############
# def solution(n, left, right):
#     answer = []
#     dim2 = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(i, n):
#             dim2[i][j] = j+1
#             dim2[j][i] = j+1

#     for row in dim2:
#         answer.extend(row)
#     return answer[left:right+1]

###################################
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row, col = i // n, i % n
        if row < col:
            answer.append(col+1)
        else:
            answer.append(row+1)
    return answer

print(solution(3,2,5))
# [3,2,2,3]
print(solution(4,7,14))
# [4,3,3,3,4,4,4,4]