def solution(n, s):
    answer  = []
    if s > n:
        answer= [s//n for _ in range(n)]
        total = sum(answer)
        idx = n-1
        while True:
            if total == s:
                return answer
            else:
                answer[idx] += 1
                total += 1
                idx -= 1 
    else:
        return [-1]