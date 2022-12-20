def solution(msg):
    answer = []
    d = dict()
    for i in range(1, 27):
        d[chr(i+64)] = i
    idx = 27
    ptr = 0
    while True:
        cnt = 1
        while ptr < len(msg):
            if msg[ptr:ptr+cnt] in d:
                if ptr + cnt == len(msg):
                    answer.append(d[msg[ptr:ptr+cnt]])
                    return answer
                else: 
                    cnt += 1 
            else:
                answer.append(d[msg[ptr:ptr+cnt-1]])
                # print("사전 추가 ", idx, " : ", msg[ptr:ptr+cnt])
                d[msg[ptr:ptr+cnt]] = idx
                idx += 1
                ptr = ptr + cnt-1
                break

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))