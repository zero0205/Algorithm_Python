def solution(tstring, variables):
    answer = ''
    # 변수 딕셔너리로
    dict = {}
    overlap = []
    for key, value in variables:
        dict[key] = value
        if value[1:-1] in dict.keys() and key == dict[value[1:-1]]:
            overlap.append(key)
            overlap.append(value[1:-1])
    ans_list = [tstring]
    str_arr = list(tstring.split())
    while True:
        change = False
        for idx in range(len(str_arr)):
            if str_arr[idx][0] != '{':
                continue
            else:
                if str_arr[idx][1:-1] in dict.keys():
                    if str_arr[idx][1:-1] in overlap:
                        continue
                    else:
                        str_arr[idx] = dict[str_arr[idx][1:-1]]
                        change = True
        if not change:
            break
        if ' '.join(str_arr) in ans_list:
            break
        ans_list.append(' '.join(str_arr))
    answer = ' '.join(str_arr)
    return answer