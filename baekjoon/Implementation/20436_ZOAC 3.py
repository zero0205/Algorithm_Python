left, right = input().split()
input_str = input()
ans = 0

# 알파벳의 키보드상 위치 찾기
def get_pos(c):
    keyboard = [['q','w','e','r','t','y','u','i','o','p'],
                ['a','s','d','f','g','h','j','k','l'],
                ['z','x','c','v','b','n','m']]
    for i in range(3):
        for j in range(len(keyboard[i])):
            if c == keyboard[i][j]:
                return [i,j]

# 손가락 이동
def finger_move(now, next):
    x, y = get_pos(now)
    nx, ny = get_pos(next)
    return abs(x-nx) + abs(y-ny) + 1

# 왼쪽인지 오른쪽인지
def leftright(c):
    left = ['q','w','e','r','t',
            'a','s','d','f','g',
            'z','x','c','v']
    if c in left:
        return 0    # 왼쪽
    else:   
        return 1    # 오른쪽

for i in range(len(input_str)):
    if leftright(input_str[i]) == 0:    # 왼쪽 손가락
        ans += finger_move(left, input_str[i])
        left = input_str[i]
    else:                               # 오른쪽 손가락
        ans += finger_move(right, input_str[i])
        right = input_str[i]
print(ans)