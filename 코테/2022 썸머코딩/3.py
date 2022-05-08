import heapq

def solution(rooms, target):
    answer = []
    room_dict = {}
    each_sit = {}
    for room in rooms:
        idx = room.find(']')
        room_num = int(room[1:idx])
        people = room[idx + 1:].split(',')
        # 각 방별 사람 딕셔너리에 저장
        room_dict[room_num] = people
        # 사람별 자리 파악
        for p in people:
            if each_sit.get(p):
                each_sit[p].append(room_num)
            else:
                each_sit[p] = [room_num]
    # 개수 세기용 힙
    sit_num = []
    for person in each_sit.keys():
        heapq.heappush(sit_num, (len(each_sit[person]), person))

    print("room_dict:", room_dict)
    print("each_sit:", each_sit)
    print("sit_num:", sit_num)

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
        for r in each_sit[now[1]]:
            now_min = min(now_min, abs(r - target))
        # 가장 가까운 방 거리, 이름 힙큐에 저장
        heapq.heappush(candidate_lst, (now_min, now[1])

    # 받기로 정해진 사람 방 줌
    room_dict[target].append(candidate[1])
    each_sit[candidate[1]]. append(target)
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