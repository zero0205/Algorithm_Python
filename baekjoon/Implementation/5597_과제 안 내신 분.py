submit = [False] * 31
for _ in range(28):
    submit[int(input())] = True

for i in range(1, 31):
    if not submit[i]:
        print(i)