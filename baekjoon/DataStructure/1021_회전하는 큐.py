from collections import deque

n, m = map(int, input().split())
pop_nums = list(map(int, input().split()))  # 뽑아내려고 하는 수의 위치
arr = deque([i for i in range(1, n+1)])  # 가장 처음 큐에서의 위치를 표시
ans = 0

for i in range(m):
    for j in range(len(arr)):   # 뽑으려는 원소의 현재 위치 찾기
        if arr[j] == pop_nums[i]:
            idx = j
            break
    if idx < len(arr)-idx:  # 2번 연산만 하는게 빠를 때
        arr.rotate(-idx)
        ans += idx
        arr.popleft()
    else:
        arr.rotate(len(arr)-idx)    # 3번 연산만 하는게 빠를 때
        ans += len(arr)-idx
        arr.popleft()
print(ans)
