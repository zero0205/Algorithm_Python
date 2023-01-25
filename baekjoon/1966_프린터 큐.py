for _ in range(int(input())):
    ans = 0
    flag = False
    # n : 문서의 개수, m : 몇번째로 인쇄되었는지 궁금한 문서의 순서
    n, m = map(int, input().split())
    # 문서의 중요도
    priority = list(map(int, input().split()))
    while not flag:
        max_pr = max(priority)  # 현재 프린터 큐에 있는 문서들 중 가장 높은 중요도
        for i in range(n):
            if max_pr == priority[i]:
                ans += 1
                priority[i] = 0         # 출력된 문서는 중요도를 0으로 갱신
                max_pr = max(priority)  # max_pr 값 갱신
                if i == m:              # 이번에 출력된 문서가 순서를 구하려던 그 문서일 때
                    print(ans)
                    flag = True
                    break