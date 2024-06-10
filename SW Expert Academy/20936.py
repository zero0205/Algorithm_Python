for tc in range(1, int(input())+1):
    n = int(input())
    arr = [-1]+list(map(int, input().split()))+[-1]

    empty = n+1   # 현재 비어있는 자리
    # 처음에 자기 위치가 아닌 상자 아무거나 빈 칸으로 옮김
    for i in range(1, n+1):
        if arr[i] != i:
            empty = i
            arr[n+1] = arr[i]
            arr[i] = -1
            break

    if empty == n+1:    # 처음에 이미 정렬이 모두 완료된 상태
        print(0)
        print()
        continue

    ans = [empty]   # 작업 순서
    while True:
        if empty == n+1:    # N+1번째가 빈 칸이 될 때마다 정렬이 완료되었는지 확인
            complete = True
            # 모두 제대로 정렬됐는지 확인
            for i in range(1, n+1):
                if arr[i] != i:
                    complete = False
                    break
            if complete:
                break
        # 빈 칸으로 옮길 상자 찾기
        try:
            idx = arr.index(empty)
        except:
            for i in range(1, n+2):
                if arr[i] != i and arr[i] != -1:
                    idx = i
                    break
        # 빈 칸(empty)으로 idx번째 칸에 있던 상자 옮김
        arr[empty] = arr[idx]
        arr[idx] = -1
        ans.append(idx)
        empty = idx
    print(len(ans))
    print(*ans)
