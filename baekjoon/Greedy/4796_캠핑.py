idx = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    ans = v//p*l + (v % p if l >= (v % p) else l)
    print(f"Case {idx}: {ans}")
    idx += 1
