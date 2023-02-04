import math

# 최대공약수 구하기 (유클리드 호제법)
def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)

# 약수 구하기
def get_divisor(num):
    res = []
    # 일단 num의 제곱근까지만 약수 구하기
    for i in range(1, int(math.sqrt(num)) + 1):  
        if num % i == 0:
           res.append(i) 
    # 제곱근까지만 구한 약수들 가지고 num을 나눠서 나머지 약수 구하기
    l = len(res)
    for i in range(l):
        res.append(num // res[i])
    return sorted(set(res))

n = int(input())
nums = list(map(int, input().split()))

if n == 2:
   for i in get_divisor(gcd(nums[0], nums[1])):
       print(i)
else:
    for i in get_divisor(gcd(nums[0], gcd(nums[1], nums[2]))):
        print(i)