# https://programmers.co.kr/learn/courses/30/lessons/64065
# 내 풀이
def solution(s):
    answer = []
    s = s.replace('{{', '')
    s = s.replace('}}', '')
    s_arr = s.split("},{")
    s_arr.sort(key=lambda x:len(x))
    s_lst_arr = []
    for i in s_arr:
        s_lst_arr.append(list(map(int, i.split(','))))
    for j in s_lst_arr:
        for el in j:
            if el not in answer:
                answer.append(el)
    return answer

# 테스트 케이스
str = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}", 
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    ]
print(solution(str[0]))
print(solution(str[1]))
print(solution(str[2]))
print(solution(str[3]))
print(solution(str[4]))