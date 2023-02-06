n = int(input())

# 팰린드롬 수인지?
def isPalindrome(n):
    num = str(n)
    reverse_num = num[::-1]
    if num == reverse_num:
        return True
    return False

# 에라토스테네스의 체
prime = [True] * 1100000
prime[1] = False
for i in range(2, int(1100000 ** 0.5) + 1):
    if prime[i]:    # i가 소수라면
        for j in range(i * 2, 1100000, i): 
            prime[j] = False    # 자신을 제외한 배수들을 지움
            
for i in range(n, 1100000):
    if str(i) == str(i)[::-1] and prime[i]:
        print(i)
        break