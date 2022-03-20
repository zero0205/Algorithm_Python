# https://www.acmicpc.net/problem/1992

n = int(input())    # 항상 2의 제곱수

film = []
for _ in range(n):
    film.append(input())

def chk(x, y, data, n):
    color = data[x][y]
    if n == 1:
        print(color, end='')
        return
    for i in range(n):
        for j in range(n):
            if color != data[x + i][y + j]:
                print("(", end='')
                chk(x, y, data, n // 2)
                chk(x , y + n // 2, data, n // 2)
                chk(x + n // 2, y, data, n // 2)
                chk(x + n // 2, y + n // 2, data, n // 2)
                print(")", end='')
                return
    print(color,end="")
    return
chk(0, 0, film, n)