def solution(bid, ask, n):
    answer = [0] * n
    # 매도는 최대한 큰 금액으로 => 내림차순 정렬
    bid = sorted(bid, reverse=True)
    # 매수는 최대한 작은 금액으로 => 오름차순 정렬
    ask = sorted(ask)
    answer[1] = bid[0] - ask[0]
    for i in range(2, n//2+1):
        answer[i] = answer[i-1] + (bid[i-1]-ask[i-1])
    return max(answer)