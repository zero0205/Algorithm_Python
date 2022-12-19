# def solution(progresses, speeds):
#     answer = []
#     publish = 0
#     prev = 0
#     while publish < len(progresses):
#         if progresses[publish] >= 100:
#             while publish != len(progresses) and progresses[publish] >= 100:
#                 publish += 1
#             if len(answer) != 0:
#                 answer.append(publish-prev)
#             else:
#                 answer.append(publish)
#         prev = publish    
#         for i in range(publish, len(progresses)):
#             progresses[i] += speeds[i]

#     return answer
##################################################
from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if cnt > 0:
            answer.append(cnt)
                
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))