import heapq

# n 입력받기
n = int(input())
# 카드 묶음 크기 입력받기
q = []
for _ in range(n):
   heapq.heappush(q, int(input())) 
   
sum = 0
while q:
    a = heapq.heappop(q)
    if q:
        b = heapq.heappop(q)
        sum += (a + b)
        heapq.heappush(q, a + b)
    else:
        print(sum)
        break