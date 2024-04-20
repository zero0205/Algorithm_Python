n = int(input())


def hanoi(n, start, other, to):
    if n == 0:
        return
    hanoi(n-1, start, to, other)  # start에서 맨 아래를 제외한 원반을 other로
    print(start, to)    # 맨 아래 원반을 to로 이동
    hanoi(n-1, other, start, to)    # other로 옮겼던 원반들 다시 to로


print(2**n-1)
hanoi(n, 1, 2, 3)
