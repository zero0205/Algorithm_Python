import heapq
from collections import defaultdict

r, c, k = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]
for i in range(3):
    arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())

# R 연산    
def row_sort():
    max_length = 0
    for i in range(100):
        num_cnt = defaultdict(int)
        for j in range(100):    # 숫자별 등장 횟수 카운트
            if arr[i][j] == 0:
                continue
            num_cnt[arr[i][j]] += 1
        
        # 수와 등장 횟수 정렬    
        heap = []
        for num, cnt in num_cnt.items():
            heapq.heappush(heap, (cnt, num))
            
        # 정렬된 결과 arr 배열에 넣기 
        idx = 0         
        while idx < 100:
            if heap:
                cnt, num = heapq.heappop(heap)
                arr[i][idx] = num
                arr[i][idx+1] = cnt
                idx += 2
                max_length = max(max_length, idx)
            else:
                arr[i][idx] = 0
                idx += 1
    return max_length
        
# C 연산    
def col_sort():
    max_length = 0
    for i in range(100):
        num_cnt = defaultdict(int)
        for j in range(100):    # 숫자별 등장 횟수 카운트
            if arr[j][i] == 0:
                continue
            num_cnt[arr[j][i]] += 1
            
        # 수와 등장 횟수 정렬    
        heap = []
        for num, cnt in num_cnt.items():
            heapq.heappush(heap, (cnt, num))
        
        # 정렬된 결과 arr 배열에 넣기
        idx = 0
        while idx < 100:
            if heap:
                cnt, num = heapq.heappop(heap)
                arr[idx][i] = num
                arr[idx+1][i] = cnt
                idx += 2
                max_length = max(max_length, idx)
            else:
                arr[idx][i] = 0
                idx += 1
    return max_length

row = 3
col = 3
for sec in range(101):
    if arr[r-1][c-1] == k:
        print(sec)
        exit()
    if row >= col:
        col = row_sort()
    else:
        row = col_sort()
    
print(-1)