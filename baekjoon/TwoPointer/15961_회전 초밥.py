##################### 시간 초과 ######################
# import sys
# input = sys.stdin.readline
 
# # 접시 수 n, 초밥 가짓수 d, 연속 접시 수 k, 쿠폰 번호 c
# n, d, k, c = map(int, input().split())
# sushi = []
# for _ in range(n):
#     sushi.append(int(input()))
    
# spin_sushi = sushi * 2
# max_kind  = 0
# for i in range(n+k):
#     set_sushi = set(spin_sushi[i:i+k])
#     max_kind = max(max_kind, len(set_sushi)+(1 if c not in set_sushi else 0))
    
# print(max_kind)
##################################################################################
from collections import defaultdict
import sys
input = sys.stdin.readline

# 접시 수 n, 초밥 가짓수 d, 연속 접시 수 k, 쿠폰 번호 c
n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))
   
sushi_dict = defaultdict(int)
sushi_dict[c] += 1  # 쿠폰

for i in range(k):
    sushi_dict[sushi[i]] += 1
    
max_kind = len(sushi_dict)
sushi = sushi * 2  # 원형 배열
for start in range(1, n):
    sushi_dict[sushi[start-1]] -= 1
    if sushi_dict[sushi[start-1]] == 0:
        del sushi_dict[sushi[start-1]]
    sushi_dict[sushi[start+k-1]] += 1
    max_kind = max(max_kind, len(sushi_dict))
    
print(max_kind)