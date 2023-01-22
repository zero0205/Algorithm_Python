from collections import deque

n = int(input())

deq = deque([i for i in range(1, n+1)])

while True:
    if len(deq) == 1:
        print(deq[0])
        break
    deq.popleft()
    deq.append(deq.popleft())