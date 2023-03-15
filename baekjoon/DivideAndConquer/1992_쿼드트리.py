n = int(input())
video = [str(input()) for _ in range(n)]

ans = ''
def check(n, r, c):
    color = video[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if color != video[i][j]:
                return False
    return True

def compress(n, r, c):
    global ans
    if check(n, r, c):
        ans += str(video[r][c])
        return 
    ans += '('
    compress(n//2, r, c)
    compress(n//2, r, c+n//2)
    compress(n//2, r+n//2, c)
    compress(n//2, r+n//2, c+n//2)
    ans += ')'
    return
    
compress(n, 0, 0)
print(ans)