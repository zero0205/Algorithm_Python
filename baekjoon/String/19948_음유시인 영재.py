input_str = input()
spaces = int(input())
alphabets = list(map(int, input().split()))

prev = '-'
title = ""
for i in range(len(input_str)):
    if input_str[i] == prev:    # 앞글자와 같은 경우
        continue
    else:   # 앞글자와 같지 않은 경우
        if input_str[i] == ' ': # 공백
            spaces -= 1
        else:   # 알파벳
            if prev == ' ' or prev == '-': # 단어의 시작
                title += input_str[i].upper()
                alphabets[ord(input_str[i].lower())-97] -= 1
            alphabets[ord(input_str[i].lower())-97] -= 1
        prev = input_str[i]

possible = True
for i in range(26):
    if alphabets[i] < 0:
        possible = False
        break
print(title if (possible and spaces >= 0) else -1)