from collections import deque

n= int(input())

def bfs(division):
    q = deque(["1"])

    while q:
        num = q.popleft()
        if int(num) % division == 0:
            return num
        q.append(num+"0")
        q.append(num+"1")

for i in range(n):
    print(bfs(int(input())))