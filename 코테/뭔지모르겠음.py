from collections import defaultdict 

def get_dist(a,b,d):
    # 글자 a와 글자 b 사이의 거리 구하기
    # d는 위치 저장된 딕셔너리
    res = 1000000
    if a not in d:
        return -1
    else:
        for a_location in d[a]:
            for b_location in d[b]:
                dist = abs(a_location[0] - b_location[0]) + abs(a_location[1] - b_location[1])
                res = min(res, dist)
        return res

def solution(word):
    keyboard = [["가","호","저","론","남","드","부","이","프","설"],
    ["알","크","청","울","키","초","트","을","배","주"],
    ["개","캠","산","대","단","지","역","구","너","양"],
    ["라","로","권","교","마","쿼","파","송","차","타"],
    ["코","불","레","뉴"," ","서","한","산","리","개"],
    ["터","강","봄","토","캠","상","호","론","운","삼"],
    ["보","람","이","경","아","두","프","바","트","정"],
    ["스","웨","어","쿼","일","소","라","가","나","도"],
    ["판","자","비","우","사","거","왕","태","요","품"],
    ["안","배","차","캐","민","광","재","봇","북","하"]]
    answer = [0, 0]

    d = defaultdict(list)

    # 각 글자의 위치 저장
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            d[keyboard[i][j]].append((i, j))

    for i in range(len(word) - 1):
        # 보드에 없는 글자인 경우
        if get_dist(word[i], word[i + 1], d) == -1:
            answer[0] += 20
        else:
            answer += get_dist(word[i], word[i + 1], d)
            answer[1] += 1
    return answer

####################################################################
from collections import defaultdict 

def get_dist(a,b,d):
    # 글자 a와 글자 b 사이의 거리 구하기
    # d는 위치 저장된 딕셔너리
    res = 1000000
    if a not in d:
        return -1
    elif b not in d:
        return 0
    else:
        for a_location in d[a]:
            for b_location in d[b]:
                dist = abs(a_location[0] - b_location[0]) + abs(a_location[1] - b_location[1])
                res = min(res, dist)
    return res

def solution(word):
    keyboard = [["가","호","저","론","남","드","부","이","프","설"],
    ["알","크","청","울","키","초","트","을","배","주"],
    ["개","캠","산","대","단","지","역","구","너","양"],
    ["라","로","권","교","마","쿼","파","송","차","타"],
    ["코","불","레","뉴"," ","서","한","산","리","개"],
    ["터","강","봄","토","캠","상","호","론","운","삼"],
    ["보","람","이","경","아","두","프","바","트","정"],
    ["스","웨","어","쿼","일","소","라","가","나","도"],
    ["판","자","비","우","사","거","왕","태","요","품"],
    ["안","배","차","캐","민","광","재","봇","북","하"]]
    answer = [0, 0]

    d = defaultdict(list)

    # 각 글자의 위치 저장
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            d[keyboard[i][j]].append((i, j))

    for i in range(len(word) - 1):
        res = get_dist(word[i], word[i + 1], d)
        # 첫번째 글자가 보드에 없는 글자인 경우
        if  res == -1:
            answer[0] += 20
        # 보드에 있는 글자
        else:
            answer[0] += res
            answer[1] += 1