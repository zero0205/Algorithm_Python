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
    q = []
    for person in personal_sit.keys():
        min_dist = int(1e9)
        # 이미 배정하려는 방에 자리가 있는 사람이면 제외
        if target in personal_sit[person]:
            continue
        # 지금 배정하려는 방으로부터 가장 가까운 방의 거리 구하기
        for r in personal_sit[person]:
            min_dist = min(min_dist, abs(r - target))
        # (배정되어 있는 자릿수, 배정할 방으로부터의 최소거리, 이름)을 최소 힙에 넣음
        heapq.heappush(q, (len(personal_sit[person]), min_dist, person))
    
    # 최소 힙에서 하나씩 pop
    while q:
        lst = heapq.heappop(q)
        answer.append(lst[2])
    return answer

# 테스트 케이스 (받을 수 있는 후보 우선순위대로 출력)
print(solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403))
#["Andy", "Louis", "Guard", "Azad"]
print(solution(["[101]Azad,Guard", "[202]Guard", "[303]Guard,Dzaz"], 202))
#["Azad", "Dzaz"]
print(solution(["[1234]None,Of,People,Here","[5678]Wow"], 1234))
#["Wow"]