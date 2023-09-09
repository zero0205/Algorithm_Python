def solution(n, m, send, errorlog):
    answer =[]
    for mail_send in send:
        server_receive = mail_send + n
        server_send = server_receive + m
        fail = False
        # 에러
        for error, sec in errorlog:
            if sec < server_receive:
                continue
            if sec > server_send:
                break
            if error == 1:  # 전송 실패
                if server_receive <= sec < server_send:
                    fail = True
                    break
            if error == 2: # 전송 지연
                if server_receive <= sec < server_send:
                    remain = (server_send - sec)
                    server_send += remain
        answer.append(server_send+n if not fail else -1)
    return answer