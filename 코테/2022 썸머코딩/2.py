# from collections import deque

# def get_distance(r, c, keyboard, target):
#     q = deque([(r, c, 0, 0)])
#     visited = [[False] * 10 for _ in range(2)]
#     visited[r][c] = True

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     while q:
#         x, y, r_dist, c_dist = q.popleft()
#         if keyboard[x][y] == target:
#             return [r_dist, c_dist]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx > 1 or ny < 0 or ny > 9: # 범위를 벗어남
#                 continue
#             if not visited[nx][ny]:
#                 if i < 2:   # 수직 이동한 경우
#                     q.append((nx, ny, r_dist + 1, c_dist))
#                 else:   # 수평 이동한 경우
#                     q.append((nx, ny, r_dist, c_dist + 1))
#                 visited[nx][ny] = True

def get_coordinate(c):
    keyboard = {
        "1":(0, 0), "2":(0, 1), "3":(0, 2), "4":(0, 3), 
        "5":(0, 4), "6":(0, 5), "7":(0, 6), "8":(0, 7), 
        "9":(0, 8), "0":(0, 9), "Q":(1, 0), "W":(1, 1), 
        "E":(1, 2), "R":(1, 3), "T":(1, 4), "Y":(1, 5), 
        "U":(1, 6), "I":(1, 7), "O":(1, 8), "P":(1, 9)}
    return keyboard[c]

def solution(line):
    answer = []
    # 손가락 초기 위치
    left = (1, 0)
    right = (1, 9)
    for c in line:
        coor = get_coordinate(c)
        left_dist = abs(left[0] - coor[0]) + abs(left[1] - coor[1])
        right_dist = abs(right[0] - coor[0]) + abs(right[1] - coor[1])
        # 두 거리가 같은 경우
        if left_dist == right_dist:
            # 왼쪽 수평 거리가 더 가까운 경우
            if abs(left[1] - coor[1]) < abs(right[1] - coor[1]):
                left = coor
                answer.append(0)
            elif abs(left[1] - coor[1]) > abs(right[1] - coor[1]):
                right = coor
                answer.append(1)
            else:   # 수평거리마저 같은 경우
                # 해당 키가 키보드 상의 왼쪽
                if coor[1] < 5:
                    left = coor
                    answer.append(0)
                else:
                    right = coor
                    answer.append(1)
        # 두 거리가 같지 않은 경우(왼손)
        elif left_dist < right_dist:
            left = coor
            answer.append(0)
        # 두 거리가 같지 않은 경우(오른)
        else:
            right = coor
            answer.append(1)
    return answer

# 테스트 케이스
print(solution("Q4OYPI"))
# [0,0,1,0,1,1]
print(solution("RYI76"))
# [0,0,1,1,0]
print(solution("64E2"))
# [1,1,1,0]