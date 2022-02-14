# 구현
# 1. 왕실의 나이트

#나이트의 현재 위치 입력
location = input()

# 나이트의 현재 위치 숫자 정보로 저장
row = int(location[1])
col = ord(location[0]) - ord('a') + 1

res = 0

# 나이트의 움직임의 경우의 수
move = [(2,1), (2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

for el in move:
  if 0 < row + el[0] < 9:
    if 0 < col + el[1] < 9:
      res += 1

print(res)