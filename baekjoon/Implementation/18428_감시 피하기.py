from itertools import combinations

n = int(input())

map_data = []   
teachers = []   
spaces = []     

for i in range(n):
    map_data.append(list(input().split()))
    for j in range(n):
        if map_data[i][j] == 'T':
            teachers.append((i,j))
        if map_data[i][j] == 'X':
            spaces.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def go_straight(x, y, dir_idx):    
    while True:
        x += dx[dir_idx]
        y += dy[dir_idx]
        if 0 <= x < n and 0 <= y < n:
            if map_data[x][y] == 'O':
                return True
            if map_data[x][y] == 'S':
                return False   
        else:
            break
    return True

def check():
    for x, y in teachers:
        for i in range(4):
            if not go_straight(x, y, i): 
                return False
    return True
                
            
for w1, w2, w3 in list(combinations(spaces, 3)):
    map_data[w1[0]][w1[1]] = 'O'
    map_data[w2[0]][w2[1]] = 'O'
    map_data[w3[0]][w3[1]] = 'O'
    
    if check():
        print("YES")
        exit()
    
    map_data[w1[0]][w1[1]] = 'X'
    map_data[w2[0]][w2[1]] = 'X'
    map_data[w3[0]][w3[1]] = 'X'
    
print("NO")