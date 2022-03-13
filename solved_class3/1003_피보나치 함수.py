fibo = [0] * 41
# 0이 호출되는 횟수 저장하는 배열
dp_0 = [0] * 41
dp_0[0] = 1
dp_0[1] = 0
dp_0[2] = 1
# 1이 호출되는 횟수 저장하는 배열
dp_1 = [0] * 41
dp_1[0] = 0
dp_1[1] = 1
dp_1[2] = 1
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if fibo[n] != 0:
        return fibo[n]
    else:
        fibo[n] = fibonacci(n-1) + fibonacci(n-2)
        dp_0[n] = dp_0[n-1] + dp_0[n-2]
        dp_1[n] = dp_1[n-1] + dp_1[n-2]
        return fibo[n]

fibonacci(40)

# t 입력받기
t = int(input())
# 테스트케이스별 실행
for _ in  range(t):
    
    # n 입력받기
    n = int(input())
    print(dp_0[n], dp_1[n])
    