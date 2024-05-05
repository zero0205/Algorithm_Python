import sys
input = sys.stdin.readline

l, w, h = map(int, input().split())
n = int(input())
cubes = []
for _ in range(n):
    a, b = map(int, input().split())
    cubes.append([2**a, b])


def dc(l, w, h, idx):   # 분할정복
    if idx == -1:   # 큐브 부족
        print(-1)
        exit()
    res = 0
    # idx번째 큐브의 필요 개수
    need = (l//cubes[idx][0])*(w//cubes[idx][0]) * (h//cubes[idx][0])
    if need <= cubes[idx][1]:   # 남은 큐브로 처리 가능
        res += need
        cubes[idx][1] -= need
    else:   # 남은 큐브 개수로는 부족 => 더 작은 큐브들로 채우기
        lack = need-cubes[idx][1]
        res += cubes[idx][1]
        cubes[idx][1] = 0
        res += dc(cubes[idx][0]*lack, cubes[idx][0], cubes[idx][0], idx-1)

    if h % cubes[idx][0] > 0:   # 위
        res += dc(l, w, h % cubes[idx][0], idx-1)
    if w % cubes[idx][0] > 0:   # 옆
        res += dc(l, w % cubes[idx][0], h-h % cubes[idx][0], idx-1)
    if l % cubes[idx][0] > 0:   # 뒤
        res += dc(l % cubes[idx][0], w-w %
                  cubes[idx][0], h-h % cubes[idx][0], idx-1)
    return res


print(dc(l, w, h, n-1))
