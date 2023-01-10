def solution(elements):
    answer = set()
    new_arr = elements + elements
    for i in range(1, len(elements)+1): # 부분 수열의 길이
        start = 0
        while start <= len(elements):
            answer.add(sum(new_arr[start:start+i]))
            start += 1
    return len(answer)

print(solution([7,9,1,1,4]))