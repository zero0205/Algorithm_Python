n = int(input())
paper = list(map(int, input().split()))

balloon = []
for i in range(n):
    balloon.append((i+1, paper[i])) # 풍선 번호, 종이에 적힌 숫자
    
idx = 0
while balloon:
    idx %= len(balloon)
    
    print(balloon[idx][0], end=" ")
    
    next_idx = idx + balloon[idx][1] + (-1 if balloon[idx][1] > 0 else 0)
    balloon.pop(idx)
    idx = next_idx