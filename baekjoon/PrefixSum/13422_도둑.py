for _ in range(int(input())):
    n, m, k = map(int, input().split())
    money = list(map(int, input().split())) * 2
    # 누적합
    acc = [0] * (n*2)
    for i in range(1, 2*n):
        acc[i] = acc[i-1] + money[(i-1) % n]
    if n == m and (acc[n]-acc[0]) < k:
        print(1)
        continue
    ans = 0
    for i in range(n):
        if (acc[i+m]-acc[i]) < k:
            ans += 1
    print(ans)
