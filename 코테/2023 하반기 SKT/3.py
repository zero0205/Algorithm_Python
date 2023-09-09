def page_move(front, back, now, idx):
    back.append(now)
    front.clear()
    return idx + 1

def page_back(front, back, now):
    front.append(now)
    return back.pop()

def page_front(front, back, now):
    back.append(now)
    return front.pop()

def solution(acts):
    answer = []
    now, idx= 0, 0
    front = []
    back = []
    for cmd, num in acts:
        for i in range(num):
            if cmd == 0:    # 페이지 이동
                idx = page_move(front, back, now, idx)
                now = idx
            elif cmd == 1 and front:    # 앞으로 이동
                now = page_front(front, back, now)
            elif cmd == -1 and back:    # 뒤로 이동
                now = page_back(front, back, now)
        answer.append(now)
    return answer