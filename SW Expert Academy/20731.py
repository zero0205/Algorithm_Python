def gcd(a, b):  # a와 b의 최대 공약수 구하기
    if b == 0:
        return a
    return gcd(b, a % b)


for tc in range(1, int(input())+1):
    n = int(input())
    board = [input() for _ in range(n)]

    possible = [True]*1000

    for i in range(n):
        for j in range(i+1, n):
            for k in range(1000):
                if possible[k]:
                    res = gcd(i+1+k, j+1+k)
                    if res == 1 and board[i][j] == '1':
                        continue
                    elif res != 1 and board[i][j] == '?':
                        continue
                    else:
                        possible[k] = False
    ans = "NO"
    for i in range(1000):
        if possible[i]:
            ans = "YES"
            break
    print(f"#{tc} {ans}")
