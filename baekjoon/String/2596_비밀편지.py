d = dict()
d['A'] = '000000'
d['B'] = '001111'
d['C'] = '010011'
d['D'] = '011100'
d['E'] = '100110'
d['F'] = '101001'
d['G'] = '110101'
d['H'] = '111010'

n = int(input())
s = input()
ans = ""
unknown = False
for i in range(n):
    char = ''
    min_diff = 6
    for k, v in d.items():
        cnt = 0  # 다른 숫자 개수
        for j in range(6):
            if v[j] != s[i*6+j]:
                cnt += 1
        if cnt < min_diff and cnt < 2:
            char = k
            min_diff = cnt
    if char != '':
        ans += char
    else:
        print(i+1)
        unknown = True
        break
if not unknown:
    print(ans)
