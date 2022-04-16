max_n = 1

def chk_grid(x, y, grid):
    nx = x
    ny = y
    nx_sum = 1
    ny_sum = 1
    ans = 0
    while True:
        nx = nx + 1
        if nx >= len(grid) or grid[nx - 1][y] != grid[nx][y]:
            n = nx_sum 
            break
        if grid[nx - 1][y] == grid[nx][y]:
            nx_sum += 1
    while True:
        ny = ny + 1
        if ny >= len(grid) or grid[x][ny - 1] != grid[x][ny]:
            n = max(n, ny_sum)
            break
        if grid[x][ny - 1] == grid[x][ny]:
            ny_sum += 1
    if n < max_n:   # 가장 큰 마름모가 아니라면 0 리턴
        return 0
    else:   # 가장 큰 마름모 가능성
        if nx_sum == max_n: # 가로 방향 마름모
            if x >= nx_sum - 1: # 위로 마름모 가능
                cnt = 1
                nx = x
                ny = y
                flag1, flag2= True, True
                # 왼쪽 위로
                while cnt <= nx_sum:
                    nx = x - 1
                    ny = y - 1
                    if not flag1:
                        break
                    for col in range(nx_sum):
                        if ny - col < 0 or grid[x][ny - col] != grid[x][y]:
                            flag1 = False
                            break
                    cnt += 1
                # 오른쪽 위로
                cnt = 1
                while cnt <= nx_sum:
                    nx = x - 1
                    ny = y + 1
                    if not flag2:
                        break
                    for col in range(nx_sum):
                        if ny + col >= len(grid) or grid[x][ny + col] != grid[x][y]:
                            flag2 = False
                            break
                    cnt += 1
                if not flag1:
                    ans += 1
                if not flag2:
                    ans += 1
            if len(grid) - x <= nx_sum:   # 아래로 마름모 가능
                cnt = 1
                nx = x
                ny = y
                flag3, flag4 = True, True
                # 왼쪽 아래로
                while cnt <= nx_sum:
                    nx = x + 1
                    ny = y - 1
                    if not flag3:
                        break
                    for col in range(nx_sum):
                        if ny - col < 0 or grid[x][ny - col] != grid[x][y]:
                            flag3 = False
                            break
                    cnt += 1
                # 오른쪽 아래로
                cnt = 1
                while cnt <= nx_sum:
                    nx = x + 1
                    ny = y + 1
                    if not flag4:
                        break
                    for col in range(nx_sum):
                        if ny + col >= len(grid) or grid[x][ny + col] != grid[x][y]:
                            flag4 = False
                            break
                    cnt += 1
                if not flag3:
                    ans += 1
                if not flag4:
                    ans += 1
        if ny_sum == max_n: # 세로 방향 마름모
            if x >= nx_sum - 1: # 위로 마름모 가능
                cnt = 1
                nx = x
                ny = y
                flag1, flag2= True, True
                # 왼쪽 위로
                while cnt <= nx_sum:
                    nx = x - 1
                    ny = y - 1
                    if not flag1:
                        break
                    for col in range(nx_sum):
                        if nx - col < 0 or grid[nx - col][y] != grid[x][y]:
                            flag1 = False
                            break
                    cnt += 1
                # 오른쪽 위로
                cnt = 1
                while cnt <= nx_sum:
                    nx = x - 1
                    ny = y + 1
                    if not flag2:
                        break
                    for col in range(nx_sum):
                        if nx + col >= len(grid) or grid[nx + col][y] != grid[x][y]:
                            flag2 = False
                            break
                    cnt += 1
                if not flag1:
                    ans += 1
                if not flag2:
                    ans += 1
            if len(grid) - x <= nx_sum:   # 아래로 마름모 가능
                cnt = 1
                nx = x
                ny = y
                flag3, flag4= True, True
                # 왼쪽 아래로
                while cnt <= nx_sum:
                    nx = x + 1
                    ny = y - 1
                    if not flag3:
                        break
                    for col in range(nx_sum):
                        if nx + col >= len(grid) or grid[nx + col][y] != grid[x][y]:
                            flag3 = False
                            break
                    cnt += 1
                # 오른쪽 아래로
                cnt = 1
                while cnt <= nx_sum:
                    nx = x + 1
                    ny = y + 1
                    if not flag4:
                        break
                    for col in range(nx_sum):
                        if nx + col >= len(grid) or grid[nx + col][y] != grid[x][y]:
                            flag4 = False
                            break
                    cnt += 1
                if not flag3:
                    ans += 1
                if not flag4:
                    ans += 1
    return ans

def solution(grid):
    answer = []
    n = 1
    prev_n = 0
    num = 0
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i == 0 and j == 0:
                prev = grid[i][j]
            else:
                if grid[i][j] != prev:
                    if n > prev_n:
                        ans += chk_grid(i, j, grid)

    return [max_n, ans]