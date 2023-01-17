def change_num(num):
    if num < 10:
        return str(num)
    elif num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'

def change(num, n):
    res = ''
    while True:
        if num // n == 0:
            res += change_num(num)
            break
        res += change_num(num % n)
        num //= n
    return res[::-1]

def solution(n, t, m, p):
    answer = ''
    cnt = 0
    while len(answer) < t * m:
        answer += change(cnt, n)
        cnt += 1
    return answer[p-1:(p-1) + t * m : m]

print(solution(2,4,2,1))
# "0111"
print(solution(16,16,2,1))
# "02468ACE11111111"
print(solution(16,16,2,2))
# "13579BDF01234567"