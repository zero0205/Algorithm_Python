from collections import deque

lines = []
while True:
    try:
        line = input()
        if not line:
            break
        lines.append(line)
    except EOFError:
        break

graph = [[] for _ in range(26)]
indegree = [0] * 26
times = [0] * 26
q = deque()
total_times = [0]*26

for line in lines:
    line = line.split()
    task = ord(line[0]) - ord('A')
    date = int(line[1])

    times[task] = date

    if len(line) > 2:
        prev_tasks = line[2]
        for prev in prev_tasks:
            prev = ord(prev) - ord('A')
            graph[prev].append(task)
            indegree[task] += 1
    else:
        q.append(task)
        total_times[task] = date

while q:
    now = q.popleft()
    for nx in graph[now]:
        indegree[nx] -= 1
        total_times[nx] = max(total_times[nx], total_times[now] + times[nx])

        if indegree[nx] == 0:
            q.append(nx)

print(max(total_times))
