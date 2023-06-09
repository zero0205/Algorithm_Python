bin_k = bin(int(input())+1)
ans = ''
for i in bin_k[3:]:
    if i == '0':
        ans += '4'
    else:
        ans += '7'
print(ans)