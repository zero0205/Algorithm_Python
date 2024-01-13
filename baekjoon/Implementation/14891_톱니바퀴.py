from collections import deque

# N극: 0, S극: 1
gears = [deque(list(input())) for _ in range(4)]
for _ in range(int(input())):   # 회전
    num, direction = map(int, input().split())
    rotation = [0] * 4
    # 시계 방향 회전은 1, 반시계는 -1
    rotation[num-1] = direction
    for i in range(num-2, -1, -1):  # num의 왼쪽 톱니바퀴
        if gears[i+1][6] != gears[i][2]:
            rotation[i] = -rotation[i+1]
        else:
            break
    for j in range(num, 4):  # num의 오른쪽 톱니바퀴
        if gears[j][6] != gears[j-1][2]:
            rotation[j] = -rotation[j-1]
        else:
            break
    for i in range(4):
        gears[i].rotate(rotation[i])

# 점수의 합 계산
ans = 0
for i in range(4):
    if gears[i][0] == '1':
        ans += 2**i

print(ans)
