from collections import deque

def next_direction(now, nx):
    if now == 'E':
        return 'left' if nx == 'N' else 'right'
    elif now == 'S':
        return 'left' if nx == 'E' else 'right'
    elif now == 'W':
        return 'left' if nx == 'S' else 'right'
    elif now == 'N':
        return 'left' if nx == 'W' else 'right'

def solution(path):
    answer = []
    prev = path[0]
    q = []
    cnt = 1
    for i in path[1:]:
        if prev == i:
            cnt += 1
        else:
            q.append((prev, cnt))
            prev = i
            cnt = 1
    if cnt != 1:
        q.append((prev, cnt))
    sec = 0
    for i in range(len(q) - 1):
        sec += q[i][1]
        if q[i][1] > 5:
            answer.append("Time " + str(sec - 5) + ": Go straight " + str(500) + "m and turn " + next_direction(q[i][0], q[i+1][0]))
        else:
            answer.append("Time " + str(sec - q[i][1]) + ": Go straight " + str(q[i][1] * 100) + "m and turn " + next_direction(q[i][0], q[i+1][0]))
    return answer