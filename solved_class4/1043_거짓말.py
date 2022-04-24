# https://www.acmicpc.net/problem/1043

import sys
input = sys.stdin.readline

# n : 사람 수 / m : 파티 수
n, m = map(int, input().split())
# 진실을 아는 사람
truth_set = set(list(map(int, input().split()))[1:])
# 각 파티(m개)마다 오는 사람 번호
parties = []
for _ in range(m):
    parties.append(list(map(int, input().split()))[1:])
    
# 진실을 아는 사람들이 계속 추가되니까 파티의 수만큼 돌아줘야함
for _ in range(m):
    for pp in parties:
        if set(pp) & truth_set:
            truth_set = set(pp) | truth_set
            
for p in parties:
    if set(p) & truth_set:
        m -= 1
        
print(m)