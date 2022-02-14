n, m = map(int, input().split())

# 맵 정보 입력받기
input_map = []
for i in range(n):
  input_map.append(list(map(int,input())))

def dfs(x, y):  # x는 행, y는 열
  # 범위 안에 있는지?
  if x < 0 or x >= n or y < 0 or y >= m:
    return False

  if input_map[x][y] == 0:
    # 방문 처리
    input_map[x][y] = 1
    # 4방향 확인
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True

  return False

res = 0 
for i in range(n):
  for j in range(m):
    if dfs(i,j):
      res += 1

print(res)