from math import sqrt

n = int(input())

# 제곱수일 때
if int(sqrt(n)) == sqrt(n):
    print(1)
    exit()
# n-i^2가 제곱수일 때, 즉, sqrt(n-i**2)가 정수일 때
for i in range(1, int(sqrt(n))+1):
    if int(sqrt(n-i**2)) == sqrt(n-i**2):
        print(2)
        exit()
# n-i^2-j^2가 제곱수일 때, 즉, sqrt(n-i**2-j**2)가 정수일 때
for i in range(1, int(sqrt(n))+1):
    for j in range(1,int(sqrt(n-i**2))+1):
        if int(sqrt(n-i**2-j**2)) == sqrt(n-i**2-j**2):
            print(3)
            exit()
print(4)