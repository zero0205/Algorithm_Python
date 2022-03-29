from collections import deque


def solution(read_id, req_info):
    answer = []
    # type : 0->구매 / 1->판매
    # amount : 1 ~ 100
    # price : 1 ~ 100
    
    # 구매/판매 요청 나누기
    buy_pending = []
    sell_pending = []
    for i in range(len(read_id)):
        if req_info[i][0] == 0: # 구매
            buy_pending.append((i, read_id[i], req_info[i][1], req_info[i][2]))
        else:   # 판매
            sell_pending.append((i, read_id[i], req_info[i][1], req_info[i][2]))
    # 정렬
    buy_pending = deque(buy_pending)
    sell_pending.sort(key=lambda x : (x[3], x[0]))  # 판매가격, 이름 오름차순 정렬
     
    # pending 상태인 판매 요청 처리
    for req in buy_pending:
        idx, name, amount, price = req
        flag = False
        for sell_req in sell_pending:
            if amount == 0: # 구매 원하는만큼 다 샀음
                break
            if price < sell_req[3]:    # 내가 구매하고자 하는 가격 이하로 팔겠다는 사람이 없음
               break
            
    return answer

print(solution(["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"], [[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]))
print(solution(["Morgan", "Teo", "Covy", "Covy", "Felix"], [[0, 10, 50], [1, 35, 70], [0, 10, 30], [0, 10, 50], [1, 11, 40]]))