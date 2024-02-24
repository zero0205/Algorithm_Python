def check(arr):
    num = arr.count(0)  # 배
    if num == 0:    # 모
        print('E')
    elif num == 1:  # 도
        print('A')
    elif num == 2:  # 개
        print('B')
    elif num == 3:  # 걸
        print('C')
    elif num == 4:  # 윷
        print('D')


for _ in range(3):
    check(list(map(int, input().split())))
