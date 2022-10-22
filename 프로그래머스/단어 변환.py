from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = dict()
    for w in words:
        visited[w] = False

    q = deque([(begin, 0)])
    visited[begin] = True

    while q:
        now, cnt = q.popleft()
        if now == target:
            return cnt
        # 문자열 비교
        for w in words:
            tmp = 0
            for i in range(len(now)):
                if w[i] != now[i]:
                    tmp += 1
            if tmp == 1 and not visited[w]:
                q.append((w, cnt + 1))
                visited[w] = True
    return 0