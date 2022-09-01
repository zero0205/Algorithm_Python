n = int(input())

pos = []
for _ in range(n):
    x, y = map(int, input().split())
    pos.append((x, y))
    
pos.append(pos[0])

answer = 0
for i in range(n):
    answer += (pos[i][0]*pos[i+1][1] - pos[i][1]*pos[i+1][0])
    
print(abs(answer/2))