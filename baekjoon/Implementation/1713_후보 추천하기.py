from heapq import heappop, heappush, heapify

n = int(input())
r = int(input())
frame = []
# 학생 게시
def add(student, num):  # 학생번호, 추천순서
    # 비어있는 사진틀이 없음
    if len(frame) == n:
        heappop(frame)
    heappush(frame, [1, num, student])  # 추천횟수, 추천순서, 학생번호
    
for idx, student in enumerate(list(map(int, input().split()))):
    find = False
    # 이미 게시된 학생인지 확인
    for i in range(len(frame)):
        if student == frame[i][2]:
            frame[i][0] += 1    # 추천 횟수 증가
            heapify(frame)
            find = True
            break
    # 아직 게시되지 않은 학생이라면
    if not find:
        add(student, idx)
        
# 학생 출력
frame.sort(key = lambda x:x[2])
for i in range(len(frame)):
    print(frame[i][2], end=" ")