input_str = input()

# k, r 개수 누적합
cnt_k = [0] * (len(input_str)+1)
cnt_r = [0] * (len(input_str)+1)
for i in range(1, len(input_str)+1):
    if input_str[i-1] == 'K':
        cnt_k[i] = cnt_k[i-1] + 1
        cnt_r[i] = cnt_r[i-1]
    else:
        cnt_k[i] = cnt_k[i-1]
        cnt_r[i] = cnt_r[i-1] + 1
# 부분 수열 중 ㅋㅋ루ㅋㅋ 문자열이 없는 경우
if cnt_r[-1] == 0:
    print(0)
    exit()
# 투포인터
ans = 0
start, end = 0, len(input_str)-1
while start <= end:
    # R 찾기
    while start < len(input_str) and input_str[start] != 'R':
        start += 1
    while end > 0 and input_str[end] != 'R':
        end -= 1
    # ㅋㅋ루ㅋㅋ 문자열 길이 구하기
    left_k = cnt_k[start]
    right_k = cnt_k[len(input_str)]-cnt_k[end+1]
    r_len = cnt_r[end+1]-cnt_r[start]
    if left_k > right_k:
        ans = max(ans, right_k*2 + r_len)
        while end > 0 and input_str[end] == 'R':
            end -= 1
    else:
        ans = max(ans, left_k*2 + r_len)
        while start < len(input_str) and input_str[start] == 'R':
            start += 1

print(ans)