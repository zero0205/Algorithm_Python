a, b = input().split()

res = []
for i in range(2, 37):
    for j in range(2, 37):
        if i == j:
            continue
        try:
            if int(a, i) == int(b, j):
                res.append((int(a, i), i, j))
        except:
            pass
if len(res) < 1:
    print("Impossible")
elif len(res) == 1:
    print(*res[0])
else:
    print("Multiple")
