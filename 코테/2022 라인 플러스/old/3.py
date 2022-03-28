def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    remote = [[] for _ in range(num_teams + 1)]   # 재택근무자 명단
    office = [[] for _ in range(num_teams + 1)]   # 오피스출근자 명단

    # employee들에 대해 출근 여부 조사
    for i in range(len(employees)):
        emp_arr = employees[i].split()
        office_yes = False
        for emp_arr_el in emp_arr[1:]:
            if emp_arr_el in office_tasks:
                office[int(emp_arr[0])].append(i + 1)
                office_yes = True
                break
        if not office_yes:
            remote[int(emp_arr[0])].append(i + 1)
    for i in range(1, num_teams + 1):
        if len(office[i]) == 0:  # 팀원이 전부 재택근무 대상
            answer.extend(remote[i][1:])
        else:
            answer.extend(remote[i])
    answer.sort()
    return answer

remote_tasks = ["development","marketing","hometask"]
office_tasks = ["recruitment","education","officetask"]
employees = ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]

print(solution(3, remote_tasks, office_tasks, employees))
