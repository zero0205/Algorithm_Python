from collections import deque

def solution(n, info):
    answer = []
    max_score = 0
    
    # 10~0점까지 라이언 화살 개수 배열, 현재 점수
    q = deque([([0 for _ in range(11)], 10)])   
    
    while q:
        arr, score = q.popleft()
        if sum(arr) == n: # 남은 화살 모두 소진
            # 점수 계산
            apeach, lion = 0, 0
            for i in range(11):
                if info[i] == 0 and arr[i] == 0: # 둘 다 한 발도 못 맞춘 경우
                    continue
                else:   # 점수 나옴
                    if info[i] >= arr[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if lion > apeach:  # 라이언이 이김
                if max_score <= (lion - apeach): # 점수차 최대이면 저장
                    max_score = lion - apeach
                    answer = []
                    answer = [i for i in arr]    
        elif sum(arr) > n:  # 화살 넘치게 쏨
            continue
        elif score == 0:    # 남은 화살 다 소진 못 하고 0점까지
            new_arr = [i for i in arr]
            new_arr[10] = n - sum(new_arr)
            q.append((new_arr, 0))
        else:
            # 어피치가 점수 가져감 (라이언이 0개 맞추기)
            new_arr = [i for i in arr]
            q.append((new_arr, score - 1))
            # 라이언이 점수 가져감 (어피치보다 1개 더 맞추기)
            new_arr2 = [i for i in arr]
            new_arr2[10-score] = info[10-score] + 1
            q.append((new_arr2, score - 1))
    if not answer:
        return [-1]
    else:
        return answer
    
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))