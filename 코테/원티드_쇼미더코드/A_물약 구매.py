import heapq, sys
input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split())) # 물약 가격

discount = []
buy = [False] * n

for i in range(1, n + 1):
    p = int(input())
    potion = []
    sum = 0
    for _ in range(p):
        a, d = map(int, input().split())    # 할인되는 물약, 할인가
        if c[a - 1] - d <= 0:   # 물약이 할인돼도 0 이하로는 불가
            d = c[a - 1] - 1    
        potion.append((a, d))
        sum += d
    heapq.heappush(discount, (-sum, i, potion))
    
ans = 0
while discount:
    total_discount, idx, potion_arr = heapq.heappop(discount)
    if buy[idx - 1]:    # 이미 구매한 포션이면 지나감
        continue
    flag = False
    possible_potion = []
    # 지금 구매한 포션으로 인해 할인되는 포션들 가격 재조정
    for d_idx, d_price in potion_arr:
        if buy[d_idx - 1]:  # 할인 목록 중 이미 구매한 포션이 있다면?
            flag = True
            break
    if flag:    # 이번에 구매 X. 힙 큐에 다시 넣고 비교
        for d_idx, d_price in potion_arr:
            if buy[d_idx - 1]:
                total_discount += d_price   # 이미 구매한 포션의 할인가는 빼주기
            else:
                if c[d_idx - 1] - d_price <= 0: # 물약이 할인돼도 0 이하로는 불가
                    d_price = c[d_idx - 1] - 1
                possible_potion.append((d_idx, d_price))
        heapq.heappush(discount, (total_discount, idx, possible_potion))
    else:   # 포션 구매
        for d_idx, d_price in potion_arr:   # 할인가로 조정
            c[d_idx - 1] -= d_price
            if c[d_idx - 1] <= 0:
                c[d_idx - 1] = 1
        ans += c[idx - 1]   # 지금 구매한 포션
        buy[idx - 1] = True # 구매한 포션 표시
         
print(ans)