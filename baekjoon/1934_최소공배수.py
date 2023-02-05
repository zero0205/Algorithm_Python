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

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a,b)) # 최소공배수