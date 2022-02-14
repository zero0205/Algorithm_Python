n = int(input())
# 각 모험가의 공포도 입력받기
scare = map(int, input().split())

# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참가
# 그룹 수의 최댓값 구하기

cnt = 0 # 그룹 수
# 1. scare 배열을 오름차순으로 정렬
scare = sorted(scare)
# 2. 배열의 마지막 원소(현재 scare 배열에서 가장 공포도가 높은 모험가의 공포도)만큼 원소들을 pop
# 3. scare이 빈배열이 될 때까지 2번 과정을 반복
while scare:
    group_num = scare.pop()
    for _ in range(group_num):
        if scare:
            scare.pop()
        else: break
    cnt += 1

# 답 출력
print(cnt)