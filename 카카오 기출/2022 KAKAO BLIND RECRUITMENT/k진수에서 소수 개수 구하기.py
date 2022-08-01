import math 

# n을 k진수로 변환한 값을 리턴
def change(n,k):    
    res = ""
    while n != 0:
        tmp = n % k
        res = str(tmp) + res
        n //= k
    return res

# 소수인지 판별
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):    # 2부터 n의 제곱근까지 확인
       if n % i == 0:
         return False
    return True
                   
def solution(n, k):
    answer = 0
    changed_num = change(n, k)  # k진수로 변환된 수(문자열)
    idx = 0
    p = ""
    if changed_num[0] == '0':   # 첫 시작도 0P0 형태인 경우
            idx += 1
    for idx in range(len(changed_num)):
        if changed_num[idx] == '0':
            if p != "" and is_prime(int(p)):
                answer += 1
            p = ""
            continue
        p += changed_num[idx]
    if p != "": # 끝부분이 0P인 경우
        if is_prime(int(p)):
            answer += 1
    return answer

print(solution(437674, 3))
print(solution(110011, 10))