##################### 틀린 코드 ##########################
# n = int(input())
# home = []
# for _ in range(n):
#     home.append(list(map(int, input().split())))
    
# move = [(0, 1), (1, 1), (1, 0)] # 오른쪽, 대각선, 아래

# pos = [(0, 0), (0, 1), 0]  # 파이프 위치 초기값, 방향
# # 파이프의 현재 방향별 이동방법의 수 (오른쪽, 대각선, 아래)
# dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]    

# def move_possible(r, c, dir):
#     possible_next_dir = []
#     # 현재 방향이 오른쪽
#     if dir == 0:
#         if home[r][c+1] == 0:      # 다음 오른쪽 가능
#             possible_next_dir.append(0)
#             if home[r+1][c+1] == 0 and home[r+1][c] == 0:   # 다음 대각선 가능
#                possible_next_dir.append(1)
#     # 현재 방향이 대각선
#     elif dir == 1:
#         if home[r][c+1] == 0:       # 다음 오른쪽 가능
#             possible_next_dir.append(0)
#             if home[r+1][c+1] == 0 and home[r+1][c] == 0:   # 다음 대각선 가능
#                possible_next_dir.append(1)
#         if home[r+1][c] == 0:       # 다음 아래 가능
#             possible_next_dir.append(2)
#     # 현재 방향이 아래
#     else:
#         if home[r][c+1] == 0 and home[r+1][c+1] == 0 and home[r+1][c] == 0:
#             possible_next_dir.append(1)
#         if home[r+1][c] == 0:
#             possible_next_dir.append(2)
#     return possible_next_dir

# # 0행은 0열 빼고 모두 오른쪽->오른쪽만 1로 초기화 (벽이 없다면)
# # 0열은 갈 방법 X
# for col in range(1, n):
#     if home[0][col] == 0:
#         dp[0][col][0] = 1

# for i in range(n-1):
#     for j in range(n-1):
#         if home[i][j] == 1:
#             continue
#         for k in range(3):  # 현재 방향
#             for nx_dir in move_possible(i, j, k):
#                 dp[i+move[nx_dir][0]][j+move[nx_dir][1]][nx_dir] += dp[i][j][k]

# print(sum(dp[-1][-1]))

##################### 정답 코드 ##########################
n = int(input())
home = []
for _ in range(n):
    home.append(list(map(int, input().split())))

# 파이프의 현재 방향별 이동방법의 수 (오른쪽, 대각선, 아래)
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]    

# 0행은 0열 빼고 모두 오른쪽->오른쪽만 1로 초기화 (벽이 만나면 더이상 못 감)
# 0열은 갈 방법 X
for col in range(1, n):
    if home[0][col] == 1:
        break
    dp[0][col][0] = 1

for i in range(1, n):
    for j in range(1, n):
        if home[i][j] == 1: # 벽이면 못 감
            continue     
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1] # 이전 방향이 오른쪽, 대각선     
        if home[i-1][j] == 0 and home[i][j-1] == 0:  # 대각선으로 이동할 때는 위아래도 확인
            dp[i][j][1] = sum(dp[i-1][j-1])         # 이전 방향이 오른쪽, 대각선, 아래                    
        dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2] # 이전 방향이 대각선, 아래

print(sum(dp[-1][-1]))