num = input()
for i in range(len(num)):
    if i == 0:
        print(bin(int(num[i]))[2:], end='')
    else:
        print(bin(int(num[i]))[2:].zfill(3), end='')        