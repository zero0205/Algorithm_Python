def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

########################################
# def solution(A,B):
#     return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))