r, c = map(int, input().split())
map_data = [list(input()) for _ in range(r)]
movings = list(map(int, list(input())))

dirs = [(0, 0), (1, -1), (1, 0), (1, 1), (0, -1),
        (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]


def manhatan_distance(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)


def solution(r, c, map_data, movings):
    js = []
    crazys = []
    for i in range(r):
        for j in range(c):
            if map_data[i][j] == "I":
                js = [i, j]
            elif map_data[i][j] == 'R':
                crazys.append([i, j])

    for moving_idx in range(len(movings)):
        # 종수 이동
        js[0] += dirs[movings[moving_idx]][0]
        js[1] += dirs[movings[moving_idx]][1]
        # 미친 아두이노가 있는 칸으로 이동한 경우에는 게임 종료
        if js in crazys:
            print(f"kraj {moving_idx+1}")
            return
        # 미친 아두이노가 종수와 가장 가까워지는 방향으로 한 칸 이동
        for c_idx in range(len(crazys)):
            shortest_dir = -1
            shortest_dist = int(1e9)
            for d in range(1, 10):
                nx = crazys[c_idx][0] + dirs[d][0]
                ny = crazys[c_idx][1] + dirs[d][1]
                dist = manhatan_distance(nx, ny, js[0], js[1])
                if 0 <= nx < r and 0 <= ny < c and dist < shortest_dist:
                    shortest_dist = dist
                    shortest_dir = d
            crazys[c_idx] = [crazys[c_idx][0]+dirs[shortest_dir]
                             [0], crazys[c_idx][1]+dirs[shortest_dir][1]]
            # 미친 아두이노가 종수의 아두이노가 있는 칸으로 이동한 경우에는 게임 종료
            if crazys[c_idx] == js:
                print(f"kraj {moving_idx+1}")
                return
        # 2개 또는 그 이상의 미친 아두이노가 같은 칸에 있는 경우에는 큰 폭발이 일어나서 그 칸의 아두이노 모두 파괴
        if len(crazys) > 1:
            crazys.sort()
            new_crazys = []
            for i in range(len(crazys)):
                if i == 0:
                    if crazys[i] != crazys[i+1]:
                        new_crazys.append(crazys[i])
                elif i == len(crazys)-1:
                    if crazys[i-1] != crazys[i]:
                        new_crazys.append(crazys[i])
                else:
                    if crazys[i-1] != crazys[i] and crazys[i] != crazys[i+1]:
                        new_crazys.append(crazys[i])
            crazys = new_crazys

    # 입력으로 주어진 방향대로 다 이동한 후의 보드의 상태 출력
    answer = [["."]*c for _ in range(r)]
    answer[js[0]][js[1]] = 'I'
    for crazy in crazys:
        answer[crazy[0]][crazy[1]] = "R"
    for i in range(r):
        print(*answer[i], sep="")


solution(r, c, map_data, movings)
