def solution(record):
    answer = []
    result = []
    user_info = dict()
    for r in record:
        cmd = r.split()
        # 입장
        if cmd[0] == "Enter":   
            # user_info에 등록
            user_info[cmd[1]] = cmd[2]
            result.append([cmd[0], cmd[1]])
        # 퇴장
        elif cmd[0] == "Leave": 
            result.append([cmd[0], cmd[1]])
        # 닉네임 변경
        else:   
            user_info[cmd[1]] = cmd[2]
    
    for i in result:
        if i[0] == "Enter":
            answer.append(user_info[i[1]]+"님이 들어왔습니다.")
        else:
            answer.append(user_info[i[1]]+"님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))