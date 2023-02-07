n = int(input())

if n == 1 or n == 3:
    print(-1)
    exit()
num2 = 0
num5 = n // 5
while True:
    num2 = (n - num5 * 5) // 2
    if num2 * 2 + num5 * 5 == n:
        print(num2 + num5)
        break
    num5 -= 1