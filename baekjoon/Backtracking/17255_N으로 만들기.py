from collections import defaultdict

n = input()
chars = defaultdict(int)
for i in list(n):
    chars[i] += 1

ans = 0
methods = []


def bt(x, path):
    global ans
    if len(x) == len(n):
        if x == n:
            ans += 1
        return
    for c, num in chars.items():
        if num == 0:
            continue
        # 양옆에 붙이기
        for nx in [c+x, x+c]:
            if n.find(nx) > -1 and path+[nx] not in methods:
                chars[c] -= 1
                methods.append(path+[nx])
                bt(nx, path+[nx])
                chars[c] += 1


bt('', [])
print(ans)
