# ### Bottom-Up 방식 ###
# def func(r, c, map_data, dp_table):
#     for i in [-1,0,1]:
#         nr = r + i  # 다음에 갈 수 있는 행
#         nc = c + 1  # 다음열
#         if nr >= n or nr < 0 or nc >= m:    # 범위를 벗어나면
#             continue
#         # 이전 값보다 크다면 값 바꿔줌
#         new_value = dp_table[r][c] + map_data[nr][nc]
#         if new_value > dp_table[nr][nc]:
#             dp_table[nr][nc] = new_value

# # t 입력받기
# t = int(input())
# for _ in range(t):
#     # n, m 입력받기
#     n, m = map(int, input().split())
#     # 금광 지도 입력받기
#     data = list(map(int,input().split()))
#     # 금광 지도 2차원 배열로 변환
#     dim2 = []
#     for i in range(0, len(data), m):
#         dim2.append(data[i:i+m])
#     dp_table = [[0] * m for _ in range(n)]  # 결과 계속 저장할 DP 테이블
#     # dp_table 1열 값들 채워줌
#     for row in range(n):
#         dp_table[row][0] = dim2[row][0]
#     # 1열 1행부터 모든 칸에 대해서 func 실행
#     for c in range(m):
#         for r in range(n):
#             func(r,c,dim2, dp_table)

#     # 마지막 열에서 최댓값 찾아서 출력
#     max_value = -1
#     for j in range(n):
#         max_value = max(max_value, dp_table[j][-1])

#     print(max_value)

##### test case #####
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

### Top-down 방식 ###
t = int(input())

def dp(r, c):
    global dim2, dp_table
    if c == 0:
        return dim2[r][c]
    if dp_table[r][c] != 0: # 이미 방문한 경우
        return dp_table[r][c]
    
    if r == 0:
        dp_table[r][c] = dim2[r][c] + max(dp(r, c-1), dp(r+1, c-1))
    elif r == n-1:
        dp_table[r][c] = dim2[r][c] + max(dp(r, c-1), dp(r-1, c-1))
    else:
        dp_table[r][c] = dim2[r][c] + max(dp(r, c-1), dp(r+1, c-1), dp(r-1,c-1))
    return dp_table[r][c]
        
for _ in range(t):
    # n, m 입력받기
    n, m = map(int, input().split())
    # 금광 지도 입력받기
    data = list(map(int,input().split()))
    # 금광 지도 2차원 배열로 변환
    dim2 = []
    for i in range(0, len(data), m):
        dim2.append(data[i:i+m])
    dp_table = [[0] * m for _ in range(n)]
    
    result = 0
    for j in range(n):
        result = max(result, dp(j, m-1))
    print(result)