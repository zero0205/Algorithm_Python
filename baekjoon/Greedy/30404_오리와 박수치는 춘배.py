n, k = map(int, input().split())
kkwaeg = list(map(int, input().split()))

idx = 0
answer = 0
while idx < n:
    time = kkwaeg[idx]
    answer += 1
    idx += 1
    while idx < n and kkwaeg[idx] <= time+k:
        idx += 1
print(answer)
