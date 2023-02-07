board = input()

def polyomino(cnt):
    if cnt % 2 == 1:    # 덮을 수 없는 경우(홀수인 경우)
        print(-1)
        exit()
    if cnt == 0:
        return ''
    tmp = ''
    a = cnt // 4
    b = (cnt - a * 4) // 2
    for _ in range(a):
        tmp += 'AAAA'
    for _ in range(b):
        tmp += 'BB'
    return tmp

cnt = 0
ans = ''
for b in board:
    if b == '.':
        ans += polyomino(cnt)
        ans += '.'
        cnt = 0 
    else:
        cnt += 1
if cnt != 0:
    ans += polyomino(cnt)
print(ans)