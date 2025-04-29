for _ in range(int(input())):
    n = int(input())
    othello_1 = input()
    othello_2 = input()

    white = 0
    black = 0
    for i in range(n):
        if othello_1[i] != othello_2[i]:
            if othello_1[i] == 'W':
                white += 1
            else:
                black += 1
    print(max(white, black))
