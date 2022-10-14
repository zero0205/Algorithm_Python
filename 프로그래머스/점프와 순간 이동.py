######### 정확성은 통과, 효율성 0점 ##########
# def solution(n):
#     ans = 0
#     dp = [int(1e9) for _ in range(n+1)]
#     dp[0], dp[1] = 0, 1
    
#     for i in range(2, n+1):
#         if i % 2 == 0:
#             dp[i] = dp[i // 2]
#         else:
#             dp[i] = dp[i-1] + 1
#     return dp[n]
###############################################
def solution(n):
    answer = 0
    while True:
        if n == 0:
            return answer
        elif n == 1:
            return answer + 1
        else:
            while n % 2 == 0:
                n //= 2
            n -= 1
            answer += 1

print(solution(5))
print(solution(6))
print(solution(5000))