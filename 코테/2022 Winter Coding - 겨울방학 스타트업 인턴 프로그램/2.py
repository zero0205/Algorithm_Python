import heapq

def update_heap(q, student_num, score):
    tmp = []
    while True:
        now_s, now_n = heapq.heappop(q)
        if -now_n == student_num:
            now_s += score
            for el in tmp:
                heapq.heappush(q, el)
            return (now_s, now_n)
        else:
            tmp.append((now_s, now_n))

def solution(n, student, point):
    answer = 0
    # 현재 우반(1)인지 열반(0)인지
    clas = [0 for _ in range(n+1)]
    # 누적점수, 번호
    # 우반
    up = [(0, -n//2)]
    for i in range(1, n//2): 
        up.append((0, -i))
        clas[i] = 1
    # 열반
    down = []
    for i in range(n//2+1, n+1):
        down.append((0, -i))

    for i in range(len(student)):
        print(student[i], clas[student[i]], point[i])
        if clas[student[i]] == 1:   # 이미 우반인 경우
            now_s, now_n = update_heap(up, student[i], point[i])
            heapq.heappush(up, (now_s, now_n))
        else:   # 열반인 경우
            now_s, now_n = update_heap(down, student[i], point[i])
            up_s, up_n = heapq.heappop(up)
            # 편성이 바뀜
            if up_s < now_s or (up_s == now_s and now_n > up_n):
                answer += 1
                heapq.heappush(up, (now_s, now_n))
                heapq.heappush(down, (up_s, up_n))
                clas[-up_n] = 0
                clas[-now_n] = 1
            # 편성 안 바뀜
            else:
                heapq.heappush(down, (now_s, now_n))
                heapq.heappush(up, (up_s, up_n))
    return answer
