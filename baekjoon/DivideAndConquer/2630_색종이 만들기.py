n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0, 0

def divide(n, r, c):
    global blue, white
    color = arr[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if arr[i][j] != color:
                divide(n//2, r, c)
                divide(n//2, r, c+n//2)
                divide(n//2, r+n//2, c)
                divide(n//2, r+n//2, c+n//2)
                return
    if color == 1:
        blue += 1
    else:
        white += 1

divide(n, 0, 0)

print(white)
print(blue)