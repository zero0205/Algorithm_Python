def solution(grade):
    answer = 0
    for i in range(len(grade)-1, 0, -1):
        if grade[i-1] > grade[i]:
            answer += grade[i-1] - grade[i] 
            grade[i-1] = grade[i]
    return answer