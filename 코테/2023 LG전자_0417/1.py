# 등차수는 몇개인가
# 등차수는 인접한 수의 차이가 일정한 수 (등차수열을 이루는 수)
n = int(input())

def chk(num):
    if num < 100:
        return True
    a = num % 10
    num //= 10
    prev = num % 10 
    diff = a - prev
    num //= 10
    while num > 0:
        now = num % 10
        if prev - now != diff:  # 등차수가 아님
            return False
        prev = now
        num //= 10
    return True
    
ans = 0
for _ in range(n):
    if chk(int(input())):
        ans += 1
        
print(ans)