n = int(input())
schedule = []
for _ in range(n):
    s, e = map(int, input().split())
    schedule.append([s, e])
    
schedule.sort(key=lambda x:(x[0], x[0]-x[1]))
calendar = [[False]*366 for _ in range(n)]
ans = 0
end_r = 0
start_c, end_c = 1, 0
# 달력에 일정 표시
for s, e in schedule:
    for i in range(n):
        if not calendar[i][s]:
            if i == 0:   # 첫째줄에 일정 들어가는 경우
                flag = False
                for j in range(n):  # 전날에 일정이 있었는지 체크
                    if calendar[j][s-1]:
                        flag = True
                        break
                if not flag:    # 새로운 시작 위치 설정
                    ans += (end_r+1) * (end_c-start_c+1)
                    start_c = s
                    end_c = e
                    end_r = 0
                else:           # 연속되게 일정이 있는 경우
                    end_r = max(end_r, i)
                    end_c = max(end_c, e)
            else:       # 첫째줄이 아닌 경우
                end_r = max(end_r, i)
                end_c = max(end_c, e)
            for j in range(s, e+1): # 일정 표시
                calendar[i][j] = True
            break    
print(ans+(end_r+1) * (end_c-start_c+1))