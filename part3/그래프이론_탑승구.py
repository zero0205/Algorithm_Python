# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 탑승구의 수 G 입력받기
g = int(input())
# 비행기의 수 P 입력받기
p = int(input())
# 각 비행기가 도킹할 수 있는 탑승구의 정보들 입력받기
parent = [i for i in range(g + 1)]
res = 0
for i in range(p):
    entrance = int(input())
    possible = find_parent(parent, entrance)
    if possible != 0:
        union_parent(parent, possible, possible - 1)    # 아직 도킹 가능 -> 왼쪽숫자와 union
        res += 1
    else:
        break
        
print(res)

### test case 1 ###
# 4
# 3
# 4
# 1
# 1

### answer 1 ###
# 2

### test case 2 ###
# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4

### answer 1 ###
# 3