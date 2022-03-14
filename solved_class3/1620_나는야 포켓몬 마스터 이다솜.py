import sys
input = sys.stdin.readline

# n : 도감에 수록된 포켓몬 개수, m : 문제 개수
n, m = map(int, input().split())
# 포켓몬 입력
pocket_dict = dict()
pocket_num = [None] * (n + 1)
for i in range(1, n + 1):
    name = input().rstrip()
    pocket_dict[name] = i
    pocket_num[i] = name

# 문제 입력
for _ in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(pocket_num[int(a)])
        continue
    else:
        print(pocket_dict[a])
        