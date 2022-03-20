def chk_own(word, goods, answer):
    is_exist = True
    length = 1
    res = ""
    while length <= len(word):
        for i in range(len(word) + 1 - length):
            for el in goods:    # 각 상품들에 대해 검색
                is_exist = False
                if word == el:  # 자기자신은 빼야됨
                    continue
                if word[i:i+length] not in el:
                    is_exist = False
                    res += word[i:i+length]
                    res += ' '
                else:
                    is_exist = True
                    res = ''
                    break
            if not is_exist:  
                answer.append(res.rstrip())  
                return answer
        length += 1
    answer.append("None")
    return answer

def solution(goods):
    answer = []
    for g in goods:
        chk_own(g, goods, answer)
    return answer

goods = input().rstrip().split()
print(solution(goods))

####################################
# pencil cilicon contrabase picturelist 

# abcdeabcd cdabe abce bcdeab