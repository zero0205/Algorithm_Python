n, m = map(int, input().split())
progress = list(map(int, input().split()))+list(map(int, input().split()))
ans = 0


def recursion(d, prev, total):
    global ans
    if d == n+1:
        if total >= m:
            ans += 1
        return
    for work in range(2):
        for place in range(3):
            if place == prev:
                recursion(d+1, place, total+progress[work*3+place]//2)
            else:
                recursion(d+1, place, total+progress[work*3+place])


recursion(1, -1, 0)
print(ans)
