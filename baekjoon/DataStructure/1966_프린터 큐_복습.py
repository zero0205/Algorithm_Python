for _ in range(int(input())):
    n, m = map(int, input().split())
    document = list(map(int, input().split()))
    
    max_priority = max(document)    # 현재 문서들 중 가장 중요도가 높은 문서의 중요도
    cnt = 0 # 문서가 출력된 횟수
    flag = True
    while flag:
        for i in range(n):
            if document[i] == max_priority:
                document[i] = -1    # 출력된 문서의 중요도를 -1로 갱신
                cnt += 1
                max_priority = max(document)
                if i == m:          # 이번에 출력된 문서가 순서를 알고 싶던 그 문서라면 출력 횟수 출력해주고 반복문 탈출
                    print(cnt)
                    flag = False
                    break