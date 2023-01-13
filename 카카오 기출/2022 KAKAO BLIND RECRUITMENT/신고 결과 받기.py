# https://programmers.co.kr/learn/courses/30/lessons/92334

# 내 풀이
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_dict = defaultdict(set)  # value의 기본 자료형을 set으로 해줌
    # 각 유저별로 신고한 id를 set 이용하여 정리
    for r in report:
        a, b = r.split()    # a: 이용자id, b: 신고한id
        report_dict[b].add(a)
    
    report_num = defaultdict(int)
    # k명 이상에게 신고당했다면 신고한 id들의 처리 결과 메일 수신 횟수 1 증가
    for a, b in report_dict.items():
        if len(b) >= k:
            for id in b:
                report_num[id] += 1
    for id in id_list:
        answer.append(report_num[id])
    return answer

# 다른 사람 풀이
def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    reported_num = {x : 0 for x in id_list}

    # id별 신고당한 횟수 카운트
    for s in set(report):
        reported_num[s.split()[1]] += 1
    # 내가 신고한 놈이 k번 이상 신고당했으면 메일 받음
    for s in set(report):
        if reported_num[s.split()[1]] >= k:
            answer[id_list.index(s.split()[0])] += 1
    return answer

# 테스트케이스 확인
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], 	["ryan con", "ryan con", "ryan con", "ryan con"], 3))

print(solution2(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution2(["con", "ryan"], 	["ryan con", "ryan con", "ryan con", "ryan con"], 3))