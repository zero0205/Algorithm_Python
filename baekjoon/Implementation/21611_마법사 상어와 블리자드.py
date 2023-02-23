from collections import deque
n, m = map(int, input().split())

ans  = [0] * 3  # 폭발한 i번 구슬 개수

# 구슬 정보 입력
marble = []
for _ in range(n):
    marble.append(list(map(int, input().strip().split())))
    
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# # 마법 시전 후 남은 구슬들 칸 순서대로 구하기 => 없어도 됨
# def get_remain_marble():
#     x, y = n//2, n//2   # 초기 위치(상어)
#     dir = 0
#     cnt = 1
#     remain_marble = deque([])
#     for _ in range(n):
#         for _ in range(2):  # 같은 거리로는 2번 이동
#             for _ in range(cnt):
#                 x += dx[dir%4]
#                 y += dy[dir%4]
#                 if 0 <= x < n and 0 <= y < n:
#                     if marble[x][y] > 0:
#                         remain_marble.append(marble[x][y])
#             dir += 1    # 왼쪽으로 회전 
#         cnt += 1    # 이동 거리 증가
#     return remain_marble
    
# 빈 칸이 생겨서 구슬이 이동
def move(func):
    marble_list = func()
    x, y = n//2, n//2   # 초기 위치(상어)
    dir = 0
    cnt = 1
    for _ in range(n):
        for _ in range(2):  # 같은 거리로는 2번 이동
            for _ in range(cnt):
                x += dx[dir%4]
                y += dy[dir%4]
                if 0 <= x < n and 0 <= y < n:
                    if marble_list:
                        marble[x][y] = marble_list.popleft()
                    else:
                        marble[x][y] = 0
            dir += 1    # 왼쪽으로 회전
        cnt += 1    # 이동 거리 증가

# 4개 이상 연속하는 구슬 폭발
def explosion():
    x, y = n//2, n//2   # 초기 위치(상어)
    dir = 0
    cnt = 1
    marble_cnt = 1
    prev = -1
    remain_marble = []
    for _ in range(n):
        for _ in range(2):  # 같은 거리로는 2번 이동
            for _ in range(cnt):
                x += dx[dir%4]
                y += dy[dir%4]
                if 0 <= x < n and 0 <= y < n:
                    if marble[x][y] == prev:
                        marble_cnt += 1
                    else:
                        if marble_cnt < 4:
                            if prev > 0:
                                for _ in range(marble_cnt):
                                    remain_marble.append(prev)
                        else:
                            ans[prev-1] += marble_cnt  # 폭발한 구슬
                        prev = marble[x][y]
                        marble_cnt = 1
            dir += 1    # 왼쪽으로 회전
        cnt += 1    # 이동 거리 증가
    
    # 1차 폭발 후 연속되는 폭발들 처리
    flag = True
    while flag: # 폭발이 더이상 없을 때까지 반복
        if not remain_marble:   # 남은 구슬이 없는 경우
            return remain_marble
        cnt = 1
        prev = remain_marble[0]
        tmp = []
        flag = False
        for m in remain_marble[1:]:
            if prev != m:
                if cnt < 4: # 4개 연속X -> 폭발 안 함
                    for _ in range(cnt):
                        tmp.append(prev)
                else:       # 4개 연속 O -> 폭발
                    flag = True
                    ans[prev-1] += cnt
                prev = m
                cnt = 1
            else:
                cnt += 1
        # 마지막 남은 구슬 처리
        if cnt < 4: # 4개 연속X -> 폭발 안 함
            for _ in range(cnt):
                tmp.append(prev)
        else:       # 4개 연속 O -> 폭발
            flag = True
            ans[prev-1] += cnt
        remain_marble = tmp
    return deque(remain_marble)

# 구슬 변화
def change():
    x, y = n//2, n//2   # 초기 위치(상어)
    dir = 0
    cnt = 1
    marble_cnt = 1
    prev = -1
    remain_marble = deque([])
    for _ in range(n):
        for _ in range(2):  # 같은 거리로는 2번 이동
            for _ in range(cnt):
                x += dx[dir%4]
                y += dy[dir%4]
                if 0 <= x < n and 0 <= y < n:
                    if marble[x][y] == prev:
                        marble_cnt += 1
                    else:
                        if prev > 0:
                            remain_marble.append(marble_cnt)
                            remain_marble.append(prev)
                        prev = marble[x][y]
                        marble_cnt = 1
            dir += 1    # 왼쪽으로 회전
        cnt += 1    # 이동 거리 증가
    return remain_marble

# 마법 시전 정보 입력
mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]
for i in range(m):
    d, s = map(int, input().strip().split())
    x, y = n//2, n//2
    for _ in range(s):  # 마법 시전
        x += mx[d-1]
        y += my[d-1]
        marble[x][y] = 0    
    # move(get_remain_marble) # 블리자드 마법 시전 직후 이동
    move(explosion)         # 4개 이상 연속하는 구슬 폭발  
    move(change)            # 구슬 변화
    # print("----%i번째 블리자드----"%(i+1))
    # for j in range(n):
    #     print(*marble[j])
    
print(ans[0] + 2 * ans[1] + 3 * ans[2])