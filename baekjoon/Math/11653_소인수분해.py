# 에라토스테네스의 체
def primeNum(n):
    num_arr = [True] * (n+1)
    for i in range(2, int(n ** 0.5) + 1):   # n의 제곱근까지만 확인
        if num_arr[i]:  # i가 소수라면
            for j in range(i * 2, n, i):    # 자기자신은 제외하고 배수들 지움
                num_arr[j] = False
    return [i for i in range(2, n + 1) if num_arr[i]]

n = int(input())
if n != 1:
    for num in primeNum(n):
        while n % num == 0:
            print(num)
            n //= num
            
# def primeNum(n):
#     num_arr = [False] * (n+1)
#     res = []
#     for i in range(2, n+1):
#         if num_arr[i]:  # 이미 지워진 수라면
#             continue
#         if n % i == 0:
#             res.append(i)
#             for j in range(i * 2, n + 1, i):    # 자기자신은 제외하고 배수들 지움
#                 num_arr[j] = True
#     return res

# n = int(input())
# if n != 1:
#     for num in primeNum(n):
#         while n % num == 0:
#             print(num)
#             n //= num