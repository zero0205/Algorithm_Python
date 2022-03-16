# https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

# 식 입력받기
arr = input().rstrip()

q = []  # 스택
num = 0

for a in arr:
    if a.isdigit():
        num *= 10
        num += int(a)
    elif a == "+":  
        q.append(num)
        q.append("+")
        num = 0
    else:   
        q.append(num)
        q.append("-")
        num = 0
q.append(num)

num, prev, res = 0, 0, 0
while q:
    if len(q) == 1: # 마지막은 숫자이니까 그거 더해줌
        res += (q.pop() + prev)
        break
    el = q.pop()
    if type(el) == int: # 숫자
        num = el
    elif el == "+": # 더하기
        prev += num
    else:   # 빼기
        prev += num
        res -= prev
        prev = 0
        
print(res)        