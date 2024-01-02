n = int(input())
sn = [input() for _ in range(n)]

for k in range(1, 101):
    new_sn = set()
    duplication = False
    for j in sn:
        own_num = j[len(j)-k:]
        if own_num in new_sn:
            duplication = True
            break
        else:
            new_sn.add(own_num)
    if duplication:
        continue
    else:
        print(k)
        break
