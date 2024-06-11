for tc in range(1, int(input())+1):
    possible = [0, 0, 0]
    s, k = input().split()
    ball = s.index('o')
    k = int(k)

    if k == 0:
        ans = ball
    elif ball == 1:
        ans = (0 if k % 2 == 1 else 1)
    elif ball == 0 or ball == 2:
        ans = (1 if k % 2 == 1 else 0)
    print(f"#{tc} {ans}")
