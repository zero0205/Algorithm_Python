n = int(input())
s = input()

e_cnt = 0
h_cnt = 0
w_cnt = 0

for i in range(len(s) -1, -1, -1):
    if s[i] == 'E':
        e_cnt += 1
    if s[i] == 'H':
        h_cnt += 1
    if e_cnt >= 2 and h_cnt >= 1:
        end = i
        break
e_cnt = 0
h_cnt = 0

for j in range(end, -1, -1):
    if s[j] == 'E':
        e_cnt += 1