n = int(input())
height = [i for i in map(int, input().split())]

total_height = sum(height)
if total_height % 3 != 0:  # 나무들의 높이의 합이 3의 배수가 아니면 NO
    print("NO")
    exit()

cnt = 0
for h in height:
    cnt += h//2 # 2만큼 성장시키는 물뿌리개 횟수

if cnt >= (total_height//3):
    print("YES")
else:
    print("NO")