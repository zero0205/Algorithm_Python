from collections import defaultdict 

def get_dist(a,b,d):
    # ���� a�� ���� b ������ �Ÿ� ���ϱ�
    # d�� ��ġ ����� ��ųʸ�
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
    keyboard = [["��","ȣ","��","��","��","��","��","��","��","��"],
    ["��","ũ","û","��","Ű","��","Ʈ","��","��","��"],
    ["��","ķ","��","��","��","��","��","��","��","��"],
    ["��","��","��","��","��","��","��","��","��","Ÿ"],
    ["��","��","��","��"," ","��","��","��","��","��"],
    ["��","��","��","��","ķ","��","ȣ","��","��","��"],
    ["��","��","��","��","��","��","��","��","Ʈ","��"],
    ["��","��","��","��","��","��","��","��","��","��"],
    ["��","��","��","��","��","��","��","��","��","ǰ"],
    ["��","��","��","ĳ","��","��","��","��","��","��"]]
    answer = [0, 0]

    d = defaultdict(list)

    # �� ������ ��ġ ����
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            d[keyboard[i][j]].append((i, j))

    for i in range(len(word) - 1):
        # ���忡 ���� ������ ���
        if get_dist(word[i], word[i + 1], d) == -1:
            answer[0] += 20
        else:
            answer += get_dist(word[i], word[i + 1], d)
            answer[1] += 1
    return answer

####################################################################
from collections import defaultdict 

def get_dist(a,b,d):
    # ���� a�� ���� b ������ �Ÿ� ���ϱ�
    # d�� ��ġ ����� ��ųʸ�
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
    keyboard = [["��","ȣ","��","��","��","��","��","��","��","��"],
    ["��","ũ","û","��","Ű","��","Ʈ","��","��","��"],
    ["��","ķ","��","��","��","��","��","��","��","��"],
    ["��","��","��","��","��","��","��","��","��","Ÿ"],
    ["��","��","��","��"," ","��","��","��","��","��"],
    ["��","��","��","��","ķ","��","ȣ","��","��","��"],
    ["��","��","��","��","��","��","��","��","Ʈ","��"],
    ["��","��","��","��","��","��","��","��","��","��"],
    ["��","��","��","��","��","��","��","��","��","ǰ"],
    ["��","��","��","ĳ","��","��","��","��","��","��"]]
    answer = [0, 0]

    d = defaultdict(list)

    # �� ������ ��ġ ����
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            d[keyboard[i][j]].append((i, j))

    for i in range(len(word) - 1):
        res = get_dist(word[i], word[i + 1], d)
        # ù��° ���ڰ� ���忡 ���� ������ ���
        if  res == -1:
            answer[0] += 20
        # ���忡 �ִ� ����
        else:
            answer[0] += res
            answer[1] += 1