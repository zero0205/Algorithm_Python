def change(s):
    num1 = s.count('1')
    num0 = len(s) - num1
    return [num0,bin(num1)[2:]]

def solution(s):
    answer = [0, 0]

    while True:
        [num0, s] = change(s)
        answer[0] += 1
        answer[1] += num0
        if len(s) == 1:
            break
    return answer