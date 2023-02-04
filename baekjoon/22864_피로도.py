a, b, c, m = map(int, input().split())

t = 0
tired = 0
work = 0
while t < 24:
    if (tired + a) > m:
        tired -= c
        if tired < 0:
            tired = 0
    else:
        tired += a
        work += b
    t += 1
        
print(work)
