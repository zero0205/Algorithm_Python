from collections import deque

def solution(k, dungeons):
    answer = 0
    q = deque([(k, [])])

    while q:
        now, visited = q.popleft()
        for i in range(len(dungeons)):
            if i not in visited and now >= dungeons[i][0]:
                q.append((now-dungeons[i][1], visited+[i]))
            else:
                answer = len(visited)       
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
# 3