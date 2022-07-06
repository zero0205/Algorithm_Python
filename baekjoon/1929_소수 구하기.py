# https://www.acmicpc.net/problem/1929

m, n = map(int, input().split())

# 에라토라테네스의 체
# 소수를 판별할 범위만큼의 배열을 할당하여, 해당하는 값을 넣어주고, 하나씩 지워감

lst = [True for _ in range(n+1)]

for i in range(2, n + 1):
    if lst[i]:
        for j in range(i * 2, n + 1, i):   # 자기 자신은 빼고 배수들만 처리
            lst[j] = False

for idx in range(m, n+1):
    if lst[idx]:
        print(idx)