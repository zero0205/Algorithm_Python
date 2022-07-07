import re

# 윤년인지 체크하는 함수
def chk_year(y):
    if y % 400 == 0:
        return True
    if y % 4 == 0 and y % 100 != 0:
        return True
    return False

# 조건을 만족하는 올바른 생년월일인지 체크하는 함수
def chk_birth(birth):
    # 형식 확인
    p = re.compile('\d{4}-\d{2}-\d{2}')
    if not p.match(birth):
        return False
    # 출생 연도 확인
    year = int(birth[:4])
    if not 1900 <= year <= 2021:
        return False
    # 출생월 확인
    month = birth[5:7]
    if not 1 <= int(month) <= 12:
        return False
    # 출생일 확인
    day = int(birth[-2:])
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        if not 1 <= day <= 31:
            return False
    if month in ['04', '06', '09', '11']:
        if not 1 <= day <= 30:
            return False
    if month == '02':
        if chk_year(year):  # 윤년인 경우
            if not 1 <= day <= 29:
                return False
        else:   # 윤년이 아닌 경우
            if not 1 <= day <= 28:
                return False
    return True

def solution(birth):
    answer = 0
    for b in birth:
        if chk_birth(b):
            answer += 1
    return answer

# 테스트 케이스
print(solution(["1899-13-31", "19001231", "2001-09-04", "1900-02-29", "2021-5-31", "1950-11-30", "1996-02-29", "1999-11-31", "2000-02-29"]))
# 4
print(solution(["-2019-12-29-", "1945--10-31", "----------", "20000-123-567"]))
# 0
