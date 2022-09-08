n = int(input())
if n == 1:
    print(0)
    exit()

# 에라토스테네스의 체
arr = [True] * (n + 1)
arr[0], arr[1] = False, False
for i in range(2, int(n**0.5)+1):
    if arr[i]:  
        for j in range(i*2, n+1, i):    
            arr[j] = False
            
# 소수들 리스트
prime_num = []
for i in range(2, n+1):
    if arr[i]:
        prime_num.append(i)

# 누적합 구하기
acc_sum = [0] * len(prime_num)
acc_sum[0] = 2
for i in range(1, len(prime_num)):
    acc_sum[i] = acc_sum[i-1] + prime_num[i]

# 투포인터
start, end = 0, 0
ans = 0
while start < len(acc_sum):
    if acc_sum[end] - acc_sum[start] + prime_num[start] == n:
        ans += 1
        start += 1
        if end < len(acc_sum) - 1:
            end += 1
    elif acc_sum[end] - acc_sum[start] + prime_num[start] < n:
        if end < len(acc_sum) - 1:
            end += 1
        else:
            break
    else:
        start += 1
        
print(ans)