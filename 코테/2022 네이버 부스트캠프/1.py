calendar = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_calendar = [[0, -1] for _ in range(13)] # 월의 시작, 마지막 기록
# total_calendar 초기화
for i in range(1, 13):
    total_calendar[i][0] = total_calendar[i-1][1] + 1
    total_calendar[i][1] = total_calendar[i][0] + calendar[i] - 1

# total 입력하면 월, 일 출력
def get_date(total):
    m = 1
    while True:
        if m > 12:
            break
        if total_calendar[m][0] <= total <= total_calendar[m][1]:
            break
        else:
            m += 1 
    d = total - total_calendar[m][0] + 1
    return [m, d]

def solution(month, day, weeks):
    answer = []

    total = total_calendar[month][0] + day - 1
    if total % 7 == 0:  # 입력한 날짜가 딱 시작일
        start_total = total
    else:
        start_total = total - total % 7
    # 시작일의 월 찾기
    start_month = get_date(start_total)[0]
    idx = start_total
    flag = False
    # 출력할 배열 만들기
    for i in range(weeks):
        if flag:
            break
        lst = []
        for j in range(7):
            # 2023년을 벗어나면 출력 X
            if idx > 364:
                flag = True
                break
            m, d = get_date(idx)
            # 시작일이면 월을 붙여주어야함
            if i == 0 and j == 0:
                lst.append(str(m) + "/" + str(d))
            # 매달 1일도 월을 붙여줌
            elif d == 1:
                lst.append(str(m) + "/" + str(d))
            else:
                lst.append(str(d))
            idx += 1
        answer.append(lst)
    return answer
