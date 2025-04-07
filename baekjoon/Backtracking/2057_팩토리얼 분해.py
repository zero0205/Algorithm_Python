n = int(input())

factorial = [1]
for i in range(1, 20):
    factorial.append(factorial[-1]*i)

answer = "NO"


def bt(num, total):
    global answer
    if total == n:
        answer = "YES"
        return
    elif total > n or num >= 20:
        return
    # num을 포함
    bt(num+1, total+factorial[num])
    # num을 포함X
    bt(num+1, total)


if n != 0:
    bt(0, 0)
print(answer)
