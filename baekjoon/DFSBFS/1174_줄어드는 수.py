from collections import deque

n = int(input())

desc = []  # 줄어드는 수
q = deque()
for i in range(10):
    desc.append(i)
    q.append(i)

while q:
    now = q.popleft()
    if len(desc) > 1_000_000:
        break
    last = now % 10
    for i in range(last):
        nx = now * 10 + i
        desc.append(nx)
        q.append(nx)

if n-1 < len(desc):
    print(desc[n-1])
else:
    print(-1)

################ DFS ###################
# n = int(input())

# desc = []


# def dfs(num):
#     desc.append(num)
#     last = num % 10
#     for i in range(last):
#         dfs(num*10+i)


# for i in range(10):
#     dfs(i)

# desc.sort()

# print(desc[n-1] if n-1 < len(desc) else -1)
