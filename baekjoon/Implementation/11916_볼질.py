n = int(input())
base = [0]*4    # 0 ~ 2번째 원소는 각각 1루, 2루, 3루, 3번째 원소는 홈
ball_count = 0
answer = 0


def wild_pitch():
    global answer
    for i in range(2, -1, -1):
        if base[i] == 1:
            base[i+1] = 1
            base[i] = 0
    if base[3] == 1:
        answer += 1
        base[3] = 0


def ball_4():
    global answer
    if base[0] == 1:
        if base[1] == 1:
            if base[2] == 1:
                answer += 1
                base[2] = 0
            base[2] = 1
            base[1] = 0
        base[1] = 1
        base[0] = 0
    base[0] = 1


for b in map(int, input().split()):
    if b == 1:  # 볼
        ball_count += 1
    elif b == 2:    # 몸에 맞는 공
        ball_count = 4
    else:   # 폭투
        ball_count += 1
        wild_pitch()

    if ball_count >= 4:
        ball_4()
        ball_count = 0

print(answer)
