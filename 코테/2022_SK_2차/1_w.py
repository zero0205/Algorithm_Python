solution.py
2022-03-19 16:44:47
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
def chk_own(word, goods, answer):
    is_exist = False
    find_len = False
    length = 0
    res = ""
    while length <= len(word):
        if find_len:
            break
        for i in range(len(word) + 1 - length):
            is_exist = False
            if find_len:
                break
            for el in goods:    # 각 상품들에 대해 검색
                if word == el:  # 자기자신은 빼야됨
                    continue
                if word[i:i+length] in el:  # 다른 상품들에 대해 검색이 된다면 더이상 볼 필요 없음
                    is_exist = True
                    length += 1
                    break
            if not is_exist:    # 고유 검색어 찾음(같은 길이에 고유 검색어 더 있을 수는 있음)
                find_len = True               
                res += word[i:i+length]
                res += ' '
    if len(res) == 0:
        answer.append("None")
    else:
        answer.append(res.rstrip())
    return answer

def solution(goods):
    answer = []
    for g in goods:
        chk_own(g, goods, answer)
    return answer
