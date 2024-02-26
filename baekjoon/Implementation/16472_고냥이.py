n = int(input())
cat = input()

alphabets = set()
partial = ""
ans = -1
for c in cat:
    if len(alphabets) < n:
        alphabets.add(c)
        partial += c
    else:
        if c in alphabets:
            partial += c
        else:
            idx = -1
            partial_set = set()
            for i in range(len(partial)-1, -1, -1):
                if len(partial_set) < n-1:
                    partial_set.add(partial[i])
                elif len(partial_set) == n-1 and partial[i] not in partial_set:
                    idx = i+1
                    break
            alphabets = partial_set
            partial = partial[idx:]+c
            alphabets.add(c)
    ans = max(ans, len(partial))
print(ans)
