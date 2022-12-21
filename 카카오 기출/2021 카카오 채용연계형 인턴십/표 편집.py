# https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, cmd):
    answer = ['O'] * n
    ptr = k
    table = {x : [x-1, x+1] for x in range(n)}  # 키값은 현재 행, 밸류의 0번째는 이전 행, 1번째는 다음 행
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    s = []
    for c in cmd:
        if len(c) > 2:
            c, num = c.split()
            num = int(num)
        if c == 'U':    # 위로 이동
            for _ in range(num):
                ptr = table[ptr][0]
        elif c == "D":  # 아래로 이동
            for _ in range(num):
                ptr = table[ptr][1]
        elif c == 'C':  # 삭제
            answer[ptr] = 'X'
            prev, next = table[ptr]
            s.append([prev, ptr, next])
            if next == None:    # 마지막 행 삭제하는 경우
                ptr = table[ptr][0]
            else:
                ptr = table[ptr][1]
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev
        else:   # 가장 최근에 삭제된 행 복구("D")
            prev, now, next = s.pop()
            answer[now] = 'O'
            if prev == None:    # 1번째 행이었던 경우
                table[next][0] = now
            elif next == None:  # 마지막 행이었던 경우
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now
            
    return "".join(answer)

# 테스트 케이스
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))