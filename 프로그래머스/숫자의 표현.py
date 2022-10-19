def solution(n):
    answer = 0
    
    acc = [0 for _ in range(n+1)]   # 누적합
    for i in range(1, n+1):
        acc[i] = i + acc[i-1]
 
    for i in range(n, -1, -1):
        for j in range(i-1, -1, -1):
            if acc[i] - acc[j] == n:
                answer += 1
                break
            elif acc[i] - acc[j] > n:
                break
    return answer