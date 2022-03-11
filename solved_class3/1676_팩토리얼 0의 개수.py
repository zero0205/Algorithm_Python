from math import factorial

# n 입력받기
n = int(input())
num = str(factorial(n))
res = 0
for i in range(len(num) - 1, 0, -1):
    if num[i] == '0':
        res += 1
    else:
        break
print(res)