import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
mosquito = defaultdict(int) # key:시각, value:모기 수
for _ in range(n):
    e, x = map(int, input().split())    # 모기 입장/퇴장 시각 
    mosquito[e] += 1
    mosquito[x] -= 1

acc = [0]
max_mos = 0
start, end = 0, 0
flag = False
key_lst = sorted(mosquito.keys())
for i in range(len(key_lst)):
    acc.append(acc[i]+mosquito[key_lst[i]])
    if max_mos < acc[i+1]:  # 최대 모기 구간 시작
        max_mos = acc[i+1]
        start = key_lst[i]
        flag = True
    if flag and acc[i+1] < max_mos: # 최대 모기 구간 끝남
        end = key_lst[i]
        flag = False

print(max_mos)
print(start, end)