import sys

n, m = map(int, sys.stdin.readline().split())
pocketmon_name = dict()
pocketmon_num = ["null"]
# 1번부터 N번까지 포켓몬 입력받기
for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    pocketmon_name[name] = i
    pocketmon_num.append(name)
    
# 문제 입력받고 대답하기
for _ in range(m):
    q = sys.stdin.readline().rstrip()
    if q.isalpha():
        print(pocketmon_name[q])
    else:
        print(pocketmon_num[int(q)])