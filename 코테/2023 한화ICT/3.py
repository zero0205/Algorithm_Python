def solution(codes):
    answer = []
    error = 0
    var = dict()
    for code in codes:
        cmd = code.split()
        # 1. 변수 생성
        if cmd[0] == "declare":
            if cmd[1] in var:   # 변수 이미 존재 => 에러
                error += 1
            else:
                var[cmd[1]] = cmd[2]
        # 업데이트
        elif cmd[0] == "update":
            if cmd[1] not in var:   # 변수이름이 존재하지 않음 => 에러
                error += 1
                continue
            # 2. 수 업데이트
            if cmd[2].isdigit():
                var[cmd[1]] = cmd[2]
            else:
                if cmd[2] not in var:   # 변수이름2가 존재하지 않음 => 에러
                    error += 1
                    continue
                var[cmd[1]] = var[cmd[2]]
        # 4. 프린트
        else:
            if cmd[1] not in var:   # 변수이름이 존재하지 않음 => 에러
                error += 1
                continue
            answer.append(int(var[cmd[1]]))  # 출력
    answer.append(error)
    return answer