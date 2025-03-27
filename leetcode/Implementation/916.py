from collections import defaultdict


def get_alphabet_dict(word):
    temp = defaultdict(int)
    for i in range(len(word)):
        temp[word[i]] += 1
    return temp


def wordSubsets(words1, words2):
    alphabet_dict = dict()
    for w2 in words2:
        temp = get_alphabet_dict(w2)
        for k, v in temp.items():
            if k not in alphabet_dict or alphabet_dict[k] < v:
                alphabet_dict[k] = v

    answer = []
    for w1 in words1:
        temp = get_alphabet_dict(w1)
        flag = True
        for k, v in alphabet_dict.items():
            if k not in temp or temp[k] < v:
                flag = False
                break
        if flag:
            answer.append(w1)
    return answer
