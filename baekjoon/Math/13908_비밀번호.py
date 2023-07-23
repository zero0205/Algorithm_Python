from math import factorial

n, m = map(int, input().split())
if m > 0:
    nums = list(map(int, input().split()))
else:
    print(10**n)
    exit()

# 포함배제의 원리
# 전체 경우의 수 - (선견지명 수를 포함하지 않고 만들기)
total = 10 ** n # 전체 경우의 수
tmp = 0
for i in range(1, m+1):
    tmp += ((-1)**(i-1)) * ((10-i) ** n) * (factorial(m)//(factorial(i)*factorial(m-i)))
print(total-tmp)