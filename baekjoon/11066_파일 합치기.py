INF = int(1e9)

for _ in range(int(input())):
    k = int(input())
    file = list(map(int, input().split()))
    
    # dp 배열 생성
    dp = [[0 for _ in range(k)] for _ in range(k)]
    
    # 우선 초기에 연속으로 된 두 파일의 합들 dp에 저장
    for i in range(k - 1):
        dp[i][i+1] = file[i] + file[i+1]
        
    # 밑에서부터 올라오며 dp 배열 업데이트
    for i in range(k-1, -1, -1):
        for j in range(k):
            if dp[i][j] == 0 and j > i:
                dp[i][j] = min([dp[i][k]+dp[k+1][j] for k in range(i, j)]) + sum(file[i:j+1])
                
    print(dp[0][k-1])