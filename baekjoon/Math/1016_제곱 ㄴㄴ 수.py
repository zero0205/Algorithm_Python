from math import sqrt, floor

min_val, max_val = map(int, input().split())
length = max_val-min_val+1

non_square = [True]*length

for i in range(2, floor(sqrt(max_val))+1):
    square_num = i**2
    if min_val % square_num == 0:
        start = (min_val//square_num)*square_num
    else:
        start = (min_val//square_num+1)*square_num
    for j in range(start, min_val+length, square_num):
        non_square[j-min_val] = False

answer = 0
for i in range(min_val, max_val+1):
    if non_square[i-min_val]:
        answer += 1
print(answer)
