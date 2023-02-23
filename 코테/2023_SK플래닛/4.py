def solution(n, m, k):
    dp = [[0] * (n+1) for _ in range(m+1)]  # 전체 너비가 m일 때 n개의 차선으로 만들 수 있는 방법의 수
    for i in range(1, k+1):
        dp[i][1] = 1    # 1개의 차선으로 만드는 경우
    for i in range(2, m+1):
        for j in range(1, k+1): # 각 차선의 너비는 최대 k
            if i-j >= 0:    
                for num in range(1, n+1):   
                    # 너비가 (i-k)이고 (num-1)개 차선으로 이루어진 도로에 
                    # 너비가 k인 차선 1개 추가해서 전체 너비 i인 도로 만들기
                    dp[i][num] += dp[i-j][num-1]
    return dp[m][n]

print(solution(3, 6, 3))
# 7
print(solution(10, 6, 5))
# 0
print(solution(3, 9, 5))
# 19