arr = input()
# 최대 수 N 구하기
if len(arr) < 10:
    max_num = len(arr)
else:
    max_num = (len(arr)-9)//2+9


def find_seq(arr, seq):
    if len(arr) == 0:
        # 1~N까지의 수로 이루어진 순열인지 확인
        sorted_seq = sorted(seq)
        possible = True
        for i in range(1, len(sorted_seq)):
            if sorted_seq[i] != sorted_seq[i-1]+1:
                possible = False
                break
        if sorted_seq[0] == 1 and possible:
            print(*seq)
            exit()
        return
    # 1글자 수
    if int(arr[0]) not in seq:
        find_seq(arr[1:], seq+[int(arr[0])])
    # 2글자 수
    if len(arr) >= 2 and int(arr[:2]) <= max_num and int(arr[:2]) not in seq:
        find_seq(arr[2:], seq+[int(arr[:2])])


find_seq(arr, [])
