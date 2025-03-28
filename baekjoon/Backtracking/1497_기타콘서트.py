n, m = map(int, input().split())

guitars = []
maximum_song = 0
for _ in range(n):
    name, songs = input().split()
    binary = ""
    for song in songs:
        binary += "1" if song == "Y" else "0"
    guitars.append((name, int(binary, 2)))
    maximum_song |= int(binary, 2)

answer = int(1e9)


def dfs(idx, guitar_cnt, song):
    global answer
    if idx == n or guitar_cnt > answer:
        return
    if song | guitars[idx][1] == maximum_song:
        answer = min(answer, guitar_cnt+1)
        return
    # 기타 포함
    dfs(idx+1, guitar_cnt+1, song | guitars[idx][1])
    # 기타 포함 X
    dfs(idx+1, guitar_cnt, song)


dfs(0, 0, 0)
print(answer if maximum_song != 0 else -1)
