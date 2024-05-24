n = int(input())


def chk(seq):
    l = len(seq)
    for i in range(2, len(seq)//2+1):
        if seq[l-i:] == seq[l-i*2:l-i]:
            return False
    return True


def bt(seq):
    if len(seq) == n:
        print(seq)
        exit()
    for i in range(1, 4):
        if seq != '' and str(i) == seq[-1]:  # 1글자 부분 수열 확인
            continue
        if chk(seq+str(i)):  # 2글자 이상 부분 수열 확인
            bt(seq+str(i))


bt('')
