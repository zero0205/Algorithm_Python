from math import sqrt

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist = sqrt((x1-x2)**2+(y1-y2)**2)
    if dist == 0:
        print(0 if r1 != r2 else -1)
    elif dist < max(r1, r2):
        if dist+min(r1, r2) < max(r1, r2):
            print(0)
        elif dist+min(r1, r2) == max(r1, r2):
            print(1)
        else:
            print(2)
    else:
        if r1+r2 < dist:
            print(0)
        elif r1+r2 == dist:
            print(1)
        else:
            print(2)
