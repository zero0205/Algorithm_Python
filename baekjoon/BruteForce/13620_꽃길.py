############# DFS ##############
def flowering(r, c):    # (r, c)는 씨앗 위치(=꽃술 위치)
    if r == 0 or r == n - 1 or c == 0 or c == n-1:  # 맨 가장자리는 꽃을 심을 수 없음
        return False
    for x, y in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr = r + x
        nc = c + y
        if nr < 0 or nr >= n or nc < 0 or nc >= n or flower[nr][nc]:
            return False    # 꽃 심기 불가능
    return True

# (r,c) 위치에 꽃 한 송이 심는데 필요한 화단 대여 비용
def get_price(r, c):
    res = garden[r][c]
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr = r + x
        nc = c + y
        res += garden[nr][nc]
    return res

# DFS
def dfs(num, price, cnt):
    global ans
    if cnt == 3:
        ans = min(ans, price)
        return
    if price > ans: # 현재 가격이 ans에 저장된 최소비용보다 크다면 더 이상 볼 필요 X
        return
    for i in range(num+1, n**2-1-n):    # 가장 끝줄은 볼 필요 없음
        r = i // n
        c = i % n
        if flowering(r, c):   # 꽃 심기 가능
            for dr, dc in [(0, 0), (0,1), (0,-1), (1,0), (-1,0)]:
                nr = r + dr
                nc = c + dc
                flower[nr][nc] = True   # 꽃 심은 자리 표시
            dfs(i, price+get_price(r, c), cnt+1)
            for dr, dc in [(0, 0), (0,1), (0,-1), (1,0), (-1,0)]:
                nr = r + dr
                nc = c + dc
                flower[nr][nc] = False

n = int(input())

garden = []
flower = [[False] * n for _ in range(n)]    # 꽃 심은 자리
ans = 3001
for _ in range(n):
    garden.append(list(map(int, input().split())))
            
dfs(n, 0, 0)    # 맨 윗줄 볼 필요 X
print(ans)

################# 완전 탐색 #######################
# from itertools import combinations

# n = int(input())
# garden = []
# for _ in range(n):
#     garden.append(list(map(int, input().split())))
    
# def flowering(arr):    # (r, c)는 씨앗 위치(=꽃술 위치)
#     res = 0
#     flower = [[False] * n for _ in range(n)]
#     for num in arr: # arr은 번호 3개 배열 ex)[7, 14, 29]
#         r = num // n
#         c = num % n
#         if c == 0 or c == n - 1:    # 맨끝 줄은 꽃이 심어질 수 없음
#             return -1
#         for x, y in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
#             nr = r + x
#             nc = c + y
#             if nr < 0 or nr >= n or nc < 0 or nc >= n or flower[nr][nc]:
#                 return -1   # 꽃 심기 불가능
#             else:
#                 res += garden[nr][nc]   # 화단 가격
#                 flower[nr][nc] = True   # 꽃 영역 표시
#     return res
    
# ans = 3001
# for arr in combinations([i for i in range(n+1, n**2-1-n)], 3):
#     if flowering(arr) >= 0:            
#         ans = min(ans, flowering(arr))
# print(ans)