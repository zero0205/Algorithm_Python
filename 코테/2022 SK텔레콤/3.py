def solution(n, plans, clients):
    answer = []
    plan_lst = []
    service = []
    for p in plans:
        lst = list(map(int, p.split()))
        data = lst[0]
        add_service = lst[1:]
        service.extend(add_service)
        plan_lst.append([data, service])
    print(plan_lst)
    return answer

print(solution(5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"]))
print(solution(4, ["38 2 3", "394 1 4"], ["10 2 3", "300 1 2 3 4", "500 1"]))