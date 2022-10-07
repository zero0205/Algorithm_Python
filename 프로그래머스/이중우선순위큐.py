import heapq

def solution(operations):
    min_q = []
    max_q = []
    for op in operations:
        if op[0] == "I":
            heapq.heappush(min_q, int(op[2:]))
            heapq.heappush(max_q, -int(op[2:]))
        elif op == "D 1":
            if not min_q:
                continue
            min_q.remove(-heapq.heappop(max_q))
        else:
            if not min_q:
                continue
            max_q.remove(-heapq.heappop(min_q))
    if min_q:
        return [-heapq.heappop(max_q), heapq.heappop(min_q)]
    else:
        return [0,0]
    
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))