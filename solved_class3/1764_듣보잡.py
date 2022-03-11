import sys
input = sys.stdin.readline
# n : 듣도 못한 사람 수, m : 보도 못한 사람 수
n, m = map(int, input().split())
# 듣도 못한 사람
hear = set()
for _ in range(n):
    hear.add(input().rstrip())
# 보도 못한 사람
see = set()
for _ in range(m):
    see.add(input().rstrip())

job = sorted(hear & see)

print(len(job))
for j in job:
    print(j)