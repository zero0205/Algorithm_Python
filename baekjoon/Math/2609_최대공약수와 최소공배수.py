# 최대공약수
def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)

# 최소공배수
def lcm(a,b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a,b)) # 최대공약수
print(lcm(a,b)) # 최소공배수

###################################
# import math

# a, b = map(int, input().split())
# print(math.gcd(a,b)) # 최대공약수
# print(math.lcm(a,b)) # 최소공배수