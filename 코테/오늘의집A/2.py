def solution(call):
    answer = ''
    call = call.lower() # 전부 소문자변환
    dict = {}
    for i in range(len(call)):
        for j in range(i + 1):
            if call[j:i + 1] in dict.keys():
                dict[call[j:i + 1]] += 1
            else:
                dict[call[j:i + 1]] = 1
    dict = list(dict.items())
    sorted(dict, key=lambda x : (x[1], len(x[0])))

    max_value = dict[0][1]  # 가장 많이 등장한 패턴의 횟수
    t = {dict[0][0]: ''}
    for i in dict[1:]:
        if max_value == i[1]:
            t[i[0]] = ''
        else:
            break
    table = str.maketrans(t)
    call.translate(table)
    return call

print(solution("abcabcdefabc"))