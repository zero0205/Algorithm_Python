n, k = map(int, input().split())
n += 1
n_arr = list(str(n))

idx = -1

while True:
    if n_arr.count('5') >= k:
        print(''.join(n_arr))
        break
    while abs(idx) < len(n_arr) and n_arr[idx] == '5':
        idx -= 1

    cur = int(''.join(n_arr))
    cur = cur + 10**(abs(idx)-1)
    n_arr = list(str(cur))
