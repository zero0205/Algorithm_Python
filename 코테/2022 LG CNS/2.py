def solution(matches, me, opp):
    answer = 0
    # 부전승 라운드 확인
    flag = True
    lucky = [False] * len(matches)
    for idx in range(4, len(matches)):
        if matches[idx] == matches[idx - 1] and flag:
            flag = False
        elif matches[idx] != matches[idx - 1]:
            if flag:    # 이전 경기가 부전승
                lucky[idx - 1] = True
            else:   # 이번 경기 부전승인지 모름. 다음 경기까지 봐야함
                if idx == len(matches) - 1: # 마지막 인덱스면 부전승임
                    lucky[idx] == True
            flag = True

    nm = matches[me]
    no = matches[opp]
    if not lucky[me]:
        answer += 1
    while True:
        if nm == no:
            return answer
        if not lucky[nm]:
            answer += 1
        nm = matches[nm]
        no = matches[no]