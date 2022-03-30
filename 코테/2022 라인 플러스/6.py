import heapq

sell_pending = []
buy_pending = []
result_dict = {}

def buy(buy_name, buy_amount, buy_price, buy_idx):
    if not sell_pending:    # 구매 가능한 게 없을 때
        heapq.heappush(buy_pending, (-buy_price, buy_idx, buy_amount, buy_name)) # 판매가격 내림차순, idx 오름차순
        return
    sell_price, sell_idx, sell_amount, sell_name = heapq.heappop(sell_pending)
    if sell_price <= buy_price: # 가격이 맞음
        amount = min(sell_amount, buy_amount)
        price = amount * sell_price
        # 결과 저장 dictionary 업데이트
        result_dict[buy_name][0] += amount
        result_dict[buy_name][1] -= price
        result_dict[sell_name][0] -= amount
        result_dict[sell_name][1] += price
        if buy_amount - amount > 0:  # 아직 더 사야할 때
            buy(buy_name, buy_amount - amount, buy_price, buy_idx)
        if sell_amount - amount > 0:  # 아직 더 팔아야할 때
            heapq.heappush(sell_pending, (sell_price, sell_idx, sell_amount - amount, sell_name))
    else:   # 가격이 맞는 요청이 없음 -> pending 상태로
        heapq.heappush(buy_pending, (-buy_price, buy_idx, buy_amount, buy_name))
        heapq.heappush(sell_pending, (sell_price, sell_idx, sell_amount, sell_name))
    return 

def sell(sell_name, sell_amount, sell_price, sell_idx):
    if not buy_pending:    # 판매자가 없을 때
        heapq.heappush(sell_pending, (sell_price, sell_idx, sell_amount, sell_name)) # 구매가격 오름차순, idx 오름차순
        return
    buy_price, buy_idx, buy_amount, buy_name = heapq.heappop(buy_pending)
    buy_price *= (-1)
    if sell_price <= buy_price: # 가격이 맞음
        amount = min(sell_amount, buy_amount)
        price = amount * sell_price
        # 결과 저장 dictionary 업데이트
        result_dict[buy_name][0] += amount
        result_dict[buy_name][1] -= price
        result_dict[sell_name][0] -= amount
        result_dict[sell_name][1] += price
        if buy_amount - amount > 0:  # 아직 더 사야할 때
            heapq.heappush(buy_pending, (-buy_price, buy_idx, buy_amount, buy_name))
        if sell_amount - amount > 0:  # 아직 더 팔아야할 때
            sell(sell_name, sell_amount - amount, sell_price, sell_idx)
    else:   # 가격이 맞는 요청이 없음 -> pending 상태로
        heapq.heappush(buy_pending, (-buy_price, buy_idx, buy_amount, buy_name))
        heapq.heappush(sell_pending, (sell_price, sell_idx, sell_amount, sell_name))
    return
    

def solution(read_id, req_info):
    answer = []
    # type : 0->구매 / 1->판매
    # amount : 1 ~ 100
    # price : 1 ~ 100
    
    # result_dict 초기화
    for id in read_id:
        result_dict[id] = [0, 0]    # 골드(amount), 실버(price)
    for i in range(len(read_id)):
        if req_info[i][0] == 0: # 구매
            buy(read_id[i], req_info[i][1], req_info[i][2], i)
        else:
            sell(read_id[i], req_info[i][1], req_info[i][2], i)
    for name in list(result_dict.keys()):
        s = name
        s += " "
        s += "+" + str(result_dict[name][0]) if result_dict[name][0] > 0 else str(result_dict[name][0])
        s += " "
        s += "+" + str(result_dict[name][1]) if result_dict[name][1] > 0 else str(result_dict[name][1])
        answer.append(s)
    answer.sort()
    return answer

# print(solution(["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"], [[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]))
print(solution(["Morgan", "Teo", "Covy", "Covy", "Felix"], [[0, 10, 50], [1, 35, 70], [0, 10, 30], [0, 10, 50], [1, 11, 40]]))