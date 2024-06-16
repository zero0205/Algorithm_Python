n = int(input())
exist = set()
for _ in range(n):
    name, io = input().split()
    if io == "enter":
        exist.add(name)
    else:
        exist.remove(name)

e_lst = sorted(list(exist))
for i in range(len(e_lst)-1, -1, -1):
    print(e_lst[i])
