# https://www.acmicpc.net/problem/1929

m, n = map(int, input().split())

# 에라토스테네스의 체
# 소수를 판별할 범위만큼의 배열을 할당하여, 해당하는 값을 넣어주고, 하나씩 지워감

lst = [True for _ in range(n+1)]
lst[1] = False
# 왜 i + 1의 제곱근까지만?
# => n의 최대 약수가 n의 제곱근 이하이므로 거기까지만 확인해도 됨
for i in range(2, int(n ** 0.5) + 1):
    if lst[i]:
        # 자기 자신은 빼고 배수들만 처리. 
        # 이때 i * i 이전의 i의 배수들은 이미 처리되었으므로 확인하지 않아도 됨
        for j in range(i * i, n + 1, i):   
            lst[j] = False

for idx in range(m, n+1):
    if lst[idx]:
        print(idx)