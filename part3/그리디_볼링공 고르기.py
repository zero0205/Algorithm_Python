from itertools import combinations
from unittest import result

# n : 볼링공 개수, m : 볼링공 최대 무게
n, m = map(int,input().split())
# 볼링공 무게 입력
weight = list(map(int, input().split()))

# 무게가 인덱스인 배열 ball 생성하여 거기에 공번호(i+1) 넣기
ball = [[] for _ in range(m+1)]
for i in range(n):
    ball[weight[i]].append(i+1) # (i+1)번 공의 무게 : weight[i]
    
# 조합 이용하여 무게 중 2개 고름. 
# ball[골라진 무게] 두 개를 곱한 값들의 합을 구함
pick = list(combinations(range(1,m+1),2))
sum = 0
for (a,b) in pick:
    sum += len(ball[a]) * len(ball[b])
    
print(sum)

#### 답지 ####
# n, m = map(int,input().split())
# data = list(map(int, input().split()))

# # 1부터 10까지의 무게를 담을 수 있는 리스트
# array = [0] * 11

# for x in data:
#     # 각 무게에 해당하는 볼링공의 개수 카운트
#     array[x] += 1
    
# result = 0
# # 1부터 m까지의 각 무게에 대하여 처리
# for i in range(1, m + 1):
#     n -= array[i]   # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
#     result += array[i] * n  # B가 선택하는 경우의 수와 곱하기
    
# print(result)