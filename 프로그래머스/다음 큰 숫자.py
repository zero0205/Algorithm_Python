def solution(n):
    answer = 0
    cnt1 = bin(n).count('1')
    
    while True:
        n += 1
        tmp = bin(n).count('1')
        if cnt1 == tmp:
            answer = n
            break
    
    return answer