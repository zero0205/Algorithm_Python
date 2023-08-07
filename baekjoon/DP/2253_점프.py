n, m = map(int, input().split())
stone = set()
jump = [[int(1e9)]*(int((2*n)**0.5)+1) for _ in range(n+1)]   # i번째 돌에 x칸 점프해서 왔을때의 점프 최소 횟수

for _ in range(m):
    stone.add(int(input())) # 못 밟는 돌

jump[1][0] = 0

for i in range(2, n+1):
    if i in stone:
        continue
    for x in range(1, (int((2*i)**0.5)+1)):
        jump[i][x] = min(jump[i-x][x-1:x+2]) + 1
            
print(min(jump[n]) if min(jump[n]) != int(1e9) else -1)