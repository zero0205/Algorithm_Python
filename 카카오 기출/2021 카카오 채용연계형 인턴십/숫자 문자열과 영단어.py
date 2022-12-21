# https://programmers.co.kr/learn/courses/30/lessons/81301
# 내 풀이
def solution(s):
    answer = 0
    num_dict = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4,
               'five': 5, 'six' : 6, 'seven' : 7, 'eight': 8, 'nine' : 9}
    num_str = ''
    for i in s:
        if i.isdigit():
            answer *= 10
            answer += int(i)
            continue
        else:
            num_str += i
            if num_str in num_dict:
                answer *= 10
                answer += num_dict[num_str]
                num_str = ''
    return answer

# 다른 사람 풀이
def solution2(s):
    num_dict = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4',
               'five': '5', 'six' : '6', 'seven' : '7', 'eight': '8', 'nine' : '9'}
    for k, v in num_dict.items():
        s = s.replace(k, v)
    return int(s)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

print(solution2("one4seveneight"))
print(solution2("23four5six7"))
print(solution2("2three45sixseven"))
print(solution2("123"))