n = int(input())
dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

# 선분 ab의 길이 ^ 2
def length(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

# 직각삼각형인지
def chk(a, b, c):
    ab = length(a, b)
    bc = length(b, c)
    ca = length(a, c)
    # a가 직각
    if ab + ca == bc:
        return True
    # b가 직각
    elif ab + bc == ca:
        return True
    # c가 직각
    elif ca + bc == ab:
        return True
    return False
    
ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if chk(dots[i], dots[j], dots[k]):
                ans += 1
print(ans)