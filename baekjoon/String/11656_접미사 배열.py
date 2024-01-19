s = input()

tail = []
for i in range(1, len(s)+1):
    tail.append(s[-i:])

tail.sort()
for t in tail:
    print(t)
