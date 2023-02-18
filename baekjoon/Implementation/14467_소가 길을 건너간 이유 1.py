n = int(input())
cow = [-1] * 11 # 소는 10마리
cnt = 0
for _ in range(n):
    num, pos = map(int, input().split())
    if cow[num] == -1:
        cow[num] = pos
    else:
        if cow[num] != pos:
            cnt += 1
            cow[num] = pos
print(cnt)