from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
for i in range(n):
    q.append(input().rstrip())

s, e = 0, n-1
while s <= e:
    if s == e:
        print(q[s], end="")
        break
    # 앞 문자 pop
    if q[s] < q[e]:
        print(q[s], end="")
        s += 1
    # 뒷 문자 pop
    elif q[s] > q[e]:
        print(q[e], end="")
        e -= 1
    # 앞뒤 같은 문자인 경우
    else:
        flag = False
        ss, ee = s+1, e-1
        # 서로 다른 문자 나올 때까지 양쪽에서 1씩 줄여감
        while ss <= ee:
            if q[ss] < q[ee]:
                print(q[s], end="")
                s += 1
                flag = True
                break
            elif q[ss] > q[ee]:
                print(q[e], end="")
                e -= 1
                flag = True
                break
            else:
                ss += 1
                ee -= 1
        # 서로 다른 문자 찾지 못했으면 그냥 앞에서 pop
        if not flag:
            print(q[s], end="")
            s += 1
    if (s+(n-1)-e) % 80 == 0:
        print()
