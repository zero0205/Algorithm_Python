import heapq

def solution(rooms, target):
    answer = []
    personal_sit = {}
    for room in rooms:
        idx = room.find(']')
        room_num = int(room[1:idx])
        people = room[idx + 1:].split(',')
        # 사람별 자리 파악
        for p in people:
            if personal_sit.get(p):
                personal_sit[p].append(room_num)
            else:
                personal_sit[p] = [room_num]
    # 개수 세기용 힙
    sit_num = []
    for person in personal_sit.keys():
        # 사람별로 현재 방까지의 최소 거리 구하기
        for r in personal_sit[person]:
            
        heapq.heappush(sit_num, (len(personal_sit[person]), person))

    candidate = ("", 10000000)
    candidate_lst = []
    
    while sit_num:
        now = heapq.heappop(sit_num)
        if candidate[0] < now[0]: # 지정 자리가 더 많은 경우 반복문 종료
            heapq.heappush(sit_num, now)
            break
        # 해당 방에 이미 자리가 있어도 후보 제외
        if now[1] in room_dict[target]:
            candidate_lst.append(now)
            continue
        now_min = 100000
        for r in personal_sit[now[1]]:
            now_min = min(now_min, abs(r - target))
        # 가장 가까운 방 거리, 이름 힙큐에 저장
        heapq.heappush(candidate_lst, (now_min, now[1])

    # 받기로 정해진 사람 방 줌
    room_dict[target].append(candidate[1])
    personal_sit[candidate[1]]. append(target)
    answer.append(candidate[1])
    # 탈락자와 자리 받은 자들 다시 힙에 넣어줌
    candidate_lst.append(candidate)
    for c in candidate_lst:
        heapq.heappush(sit_num, c)
    return answer

# 테스트 케이스 (받을 수 있는 후보 우선순위대로 출력)
print(solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403))
#["Andy", "Louis", "Guard", "Azad"]
print(solution(["[101]Azad,Guard", "[202]Guard", "[303]Guard,Dzaz"], 202))
#["Azad", "Dzaz"]
print(solution(["[1234]None,Of,People,Here","[5678]Wow"], 1234))
#["Wow"]