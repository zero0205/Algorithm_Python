import re

def solution(logs):
    answer = 0
    p = re.compile("team_name : [^a-zA-Z]+ application_name : [^a-zA-Z]+ error_level : [^a-zA-Z]+ message : [^a-zA-Z]+")
    
    for log in logs:
        if len(log) > 100:
            answer += 1
            continue
        m = p.match(log)
        if m == None:
            answer += 1
    return answer

logs = [
    "team_name : db application_name : dbtest error_level : info message : test", 
    "team_name : test application_name : I DONT CARE error_level : error message : x", 
    "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", 
    "team_name : oberervability application_name : LogViewer error_level : error"
    ]
print(solution(logs))