from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
a_arr = list(map(int, input().split()))
m = int(input())
b_arr = list(map(int, input().split()))

# A 배열의 부분합을 딕셔너리에 개수만 저장
a_dict = defaultdict(int)
for i in range(n):
    for j in range(i, n):
        a_dict[sum(a_arr[i:j+1])] += 1
# B 배열의 부분합은 구하는 동시에 t에서 그 값을 빼서 A 부분합 딕셔너리 인덱스로 사용       
res = 0
for i in range(m):
    for j in range(i, m):
        res += a_dict[t - sum(b_arr[i:j+1])]
    
print(res)