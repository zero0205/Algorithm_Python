n = int(input())
# 에라토라테네스의 체
prime_num = [True] * (1100000 + 1)
prime_num[0], prime_num[1] = False, False
for i in range(2, int(1100000 ** 0.5) + 1):
    if prime_num[i]:
        for j in range(i * 2, 1100000 + 1, i):
            prime_num[j] = False
            
for num in range(n, 1100000):
    if not prime_num[num]:  # 소수 아니면 pass
        continue
    if str(num) == str(num)[::-1]:
        print(num)
        exit()