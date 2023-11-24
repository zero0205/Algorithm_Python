from math import sqrt

a, b = map(int, input().split())

def palindrom(num):
    str_num = str(num)
    l = len(str_num)
    for i in range(l):
        if str_num[i] != str_num[l-1-i]:
            return False
    return True

for i in range(a, min(b+1, 10_000_000)):
    flag = True
    if palindrom(i):
        for j in range(2, int(sqrt(i))+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i)
            
print(-1)