import re

def solution(logs):
    answer = 0
    p = re.compile("team_name : [a-zA-Z]+ application_name : [a-zA-Z]+ error_level : [a-zA-Z]+ message : [a-zA-Z]+")
    
    for log in logs:
        if len(log) > 100:
            answer += 1
            continue
        m = p.match(log)
        if m == None:
            answer += 1
        else:
            print(m)
    return answer

# logs = [
#     "team_name : db application_name : dbtest error_level : info message : test", 
#     "team_name : test application_name : I DONT CARE error_level : error message : x", 
#     "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", 
#     "team_name : oberervability application_name : LogViewer error_level : error"
#     ]

logs = [
    "team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", 
    "no such file or directory", 
    "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", 
    "team_name : recommend application_name : recommend error_level : info message : Success!", 
    "   team_name : db application_name : dbtest error_level : info message : test", 
    "team_name    : db application_name : dbtest error_level : info message : test", 
    "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"
    ]
print(solution(logs))