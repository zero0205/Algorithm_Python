n = int(input())

answer = 0


def bt(n, chosen):
    global answer
    if len(chosen) == n:
        if sum(chosen) % 3 == 0:
            answer += 1
        return

    start = 1 if len(chosen) == 0 else 0
    for i in range(start, 3):
        bt(n, chosen+[i])


bt(n, [])
print(answer)
