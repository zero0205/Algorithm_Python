import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
a = defaultdict(str)
for _ in range(n):
    k, v = input().split('=')
    a[k] = v

m = int(input())
create = []
modify = []
for _ in range(m):
    k, v = input().split('=')
    if k in a:
        if v != a[k]:    # 변경된 경우
            modify.append(k)
        del a[k]
        continue
    else:              # 생성
        create.append(k)
        continue

# 삭제된 경우는 a dict에 남아있을것
print(len(create), *sorted(create))
print(len(a), *sorted(a.keys()))
print(len(modify), *sorted(modify))