n, m = map(int, input().split())
hear = set()
see = set()
for _ in range(n):
    hear.add(input())
for _ in range(m):
    see.add(input())
ans = hear & see
print(len(ans))
for name in sorted(ans):
    print(name)