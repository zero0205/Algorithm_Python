import sys
input = sys.stdin.readline
from collections import deque, defaultdict
 
n, t = map(int, input().split())
wall = defaultdict(list)
for _ in range(n):
    x, y = map(int, input().split())
    wall[y].append(x)

q = deque([(0, 0, 0)])

while q:
    x, y, cnt = q.popleft()
    if y == t:  # 정상에 오르기 성공
        print(cnt)
        exit()
    for b in range(-2, 3):
        if y+b in wall:
            remove_lst = []
            for a in wall[y+b]:
                if abs(a-x) <= 2:
                    q.append((a,y+b,cnt+1))
                    remove_lst.append(a)
            # 이용한 홈 리스트에서 제거 -> 방문처리
            for r in remove_lst:
                wall[y+b].remove(r)
print(-1)