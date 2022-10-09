from collections import defaultdict

def check(events, event_lst):
    for i in range(len(event_lst)):
        if events[i] != event_lst[i]:
            return False
    return True

def solution(logs, events):
    answer = []
    u_log = defaultdict(list)
    for log in logs:
        t, uid, e = log.split()
        u_log[uid].append(e)

    for k, v in u_log.items():
        if not check(events, v):
            answer.append(k)
    if answer:
        return sorted(answer)
    else:
        return ["-1"]