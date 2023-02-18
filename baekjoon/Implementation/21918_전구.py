n, m = map(int, input().split())
light = list(map(int, input().split()))

def cmd(a,b,c):
    if a == 1:
        light[b-1] = c
    elif a == 2:
        for i in range(b, c+1):
            if light[i-1] == 0:
                light[i-1] = 1
            else:
                light[i-1] = 0
    elif a == 3:
        for i in range(b, c+1):
            light[i-1] = 0
    else:
        for i in range(b, c+1):
            light[i-1] = 1
            
for i in range(m):
    a, b, c = map(int, input().split())
    cmd(a,b,c)

print(*light)