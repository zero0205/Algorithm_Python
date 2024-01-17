for _ in range(int(input())):
    d, n = map(int, input().split())
    arr = list(map(int, input().split()))

    mod = [0]*d
    sum = 0
    ans = 0
    for a in arr:
        sum = (a+sum) % d   # (sum+현재 수 a)를 d로 나눴을 때의 나머지
        # d로 나머지가 같은 애들끼리 뺄셈을 하면 d의 배수가 됨
        ans += mod[sum]
        mod[sum] += 1
    ans += mod[0]
    print(ans)
