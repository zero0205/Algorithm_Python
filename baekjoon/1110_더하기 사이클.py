n = int(input())

cnt = 0
res = n
while True:
    if cnt != 0 and res == n:
        print(cnt)
        break
    cnt += 1
    if res < 10:
        res = res * 11
    else:
        new_sum = (res // 10) + (res % 10)
        res = (res % 10) * 10 + (new_sum % 10)