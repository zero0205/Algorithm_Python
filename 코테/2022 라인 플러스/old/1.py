def chk(str):
    for s in str:
        if not ('A' <= s <= 'Z' or 'a' <= s <= 'z'):
            return False
    return True

def solution(logs):
    answer = -1
    for log in logs:
        if len(log) > 100:  # 로그 길이 초과
            answer += 1
            continue
        log_arr = log.split(" : ")
        if len(log_arr) != 5:   # 요소들 개수가 안 맞음
            answer += 1
            continue
        if log_arr[0] != "team_name":
            answer += 1
            continue
        t = log_arr[1].split()
        if (t[1] != "application_name") or (len(t) != 2) or chk(t[0]):
            answer += 1
            continue
        a = log_arr[2].split()
        if (a[1] != "error_level") or (len(a) != 2) or chk(a[0]):
            answer += 1
            continue
        e = log_arr[3].split()
        if (e[1] != "message") or (len(e) != 2) or chk(e[0]):
            answer += 1
            continue
        m = log_arr[4].split()
        if (len(m) != 1) or chk(m[0]):
            answer += 1
            continue
    return answer

log_arr = "team_name : db application_name : dbtest error_level : info message : test".split(":")
# log_arr = map(strip, log_arr)
print(log_arr)