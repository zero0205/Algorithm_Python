for _ in range(int(input())):
    n, m = input().split()
    zero = 0
    one = 0
    for i in range(len(n)):
        if n[i] != m[i]:
            if n[i] == '0':
                zero += 1
            else:
                one += 1
    print(max(zero, one))
