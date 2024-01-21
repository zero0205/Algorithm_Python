from bisect import insort
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

jbnu = dict()
keys = []
# 초기 데이터 입력
for _ in range(n):
    key, value = map(int, input().split())
    jbnu[key] = value
    keys.append(key)

keys.sort()


def search(target):  # 검색
    s, e = 0, len(keys)-1
    gap = sys.maxsize
    res = [-1]
    while s <= e:
        mid = (s+e)//2
        if jbnu[keys[mid]] == target:
            return [target]
        else:
            mid_key = keys[mid]
            if abs(mid_key-target) <= k:
                if abs(mid_key-target) < gap:
                    gap = abs(mid_key-target)
                    res = [mid_key]
                elif abs(mid_key-target) == gap:
                    res.append(mid_key)
            if mid_key < target:
                s = mid+1
            else:
                e = mid-1
    return res


# 명령 입력
for _ in range(m):
    cmd = list(map(int, input().split()))
    res = search(cmd[1])
    if cmd[0] == 1:  # 데이터 추가
        if res[0] != -1 and jbnu[res[0]] == cmd[1]:
            continue
        else:
            insort(keys, cmd[1])
            jbnu[cmd[1]] = cmd[2]
    elif cmd[0] == 2:   # 데이터 변경
        res = search(cmd[1])
        if res[0] >= 0 and len(res) == 1:
            jbnu[res[0]] = cmd[2]
    else:   # 데이터 출력
        res = search(cmd[1])
        if len(res) > 1:
            print("?")
        else:
            if res[0] >= 0:
                print(jbnu[res[0]])
            else:
                print(-1)
