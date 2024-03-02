num = input()
zero_idx = num.find('0')
if zero_idx == -1 or int(num) % 3 != 0:
    print(-1)
else:
    num_lst = sorted(list(num), reverse=True)
    print(''.join(num_lst))
