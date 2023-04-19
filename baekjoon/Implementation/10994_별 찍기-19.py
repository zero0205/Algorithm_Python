# i번째 사각형 한 변 길이 : 4(i-1)+1
n = int(input())

length = 4*(n-1)+1
stars = [[' '] * length for _ in range(length)]

def draw(num):
    if num == 1:
        stars[length//2][length//2] = "*"
        return
    # 한 변의 길이
    l = 4 * (num-1) + 1
    gap = (n-num)*2
    # 맨윗줄, 맨아랫줄
    for i in range(l):
        stars[length//2-l//2][gap+i] = '*'
        stars[length//2+l//2][gap+i] = '*'
    # 양옆        
    for i in range(l):
        stars[gap+i][gap] = "*"
        stars[gap+i][length-gap-1] = "*"
    return draw(num-1)

draw(n)
        
for i in range(length):
    for j in range(length):
        print(stars[i][j], end='')
    print()