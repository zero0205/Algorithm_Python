import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map_data = []
for _ in range(n):
    map_data.append(input())
    
arr = [i for i in range(n * m)]
ans = 0

def move(num):
    x = num // m
    y = num % m
    if map_data[x][y] == 'U':
        return (x - 1) * m + y
    elif map_data[x][y] == 'D':
        return (x + 1) * m +  y
    elif map_data[x][y] == 'L':
        return x * m + (y - 1)
    else:
        return x * m + (y + 1)

def find_cycle(num):
    global ans
    
    if arr[num] != num: # 이미 방문한 칸
        return
    nx = num
    while True:
        nx = move(nx)
        if arr[nx] == num:   # 사이클 완성
            ans += 1
            return
        else: 
            if arr[nx] != nx:   # 다른 사이클 만남
                return
        arr[nx] = num
       
for num in range(n*m):
    find_cycle(num)

print(ans)

#########################################
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# map_data = []
# for _ in range(n):
#     map_data.append(list(input()))
    
# parent = [i for i in range(n * m)]

# def find(parent, x):
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])
#     return parent[x]

# def union(parent, a, b):
#     a = find(parent, a)
#     b = find(parent, b)
    
#     if a == b:
#         return True
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#     return False

# def move(num):
#     x = num // m
#     y = num % m
#     if map_data[x][y] == 'U':
#         return (x - 1) * m + y
#     elif map_data[x][y] == 'D':
#         return (x + 1) * m + y
#     elif map_data[x][y] == 'L':
#         return x * m + (y - 1)
#     else:
#         return x * m + (y + 1)
       
# ans = 0 
# visited = set()

# for num in range(n*m):
#     nx = move(num)
#     union(parent, num, nx)
    
# for num in range(n * m):
#     if find(parent, parent[num]) in visited:
#             ans += 1
#             visited.add(parent[num])
            
# print(len(visited))
# print(ans)