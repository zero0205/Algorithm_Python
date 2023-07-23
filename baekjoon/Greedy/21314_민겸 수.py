mg = input()

max_v, min_v = '', ''
m = 0
for i in range(len(mg)):
    if mg[i] == 'M':
        m += 1
    elif mg[i] == 'K':
        if m > 0:
            max_v += str(5*(10**m))
            min_v += str(10**m+5)
        else:
            max_v += '5'
            min_v += '5'
        m = 0

# 끝부분이 M으로 끝나는 경우
if m > 0:
    for i in range(m):
        max_v += '1'
    min_v += str(10**(m-1))
    
print(max_v)
print(min_v)