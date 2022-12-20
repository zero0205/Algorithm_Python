def remove_possible(x, y, board):
    tmp = board[x][y]
    if tmp == None: # 빈 칸
        return None
    for i in range(2):
        for j in range(2):
            # 지워질 수 없는 블록이라면 None을 리턴
            if board[x+i][y+j] != tmp:
                return None
    # 지울 수 있는 블록들의 좌표를 리턴
    return [(x,y),(x,y+1),(x+1,y),(x+1,y+1)]

def solution(m, n, board):
    answer = 0
    
    board = [[board[x][y] for y in range(n)] for x in range(m)]

    while True:
        rmv_block = set()
        for x in range(m-1):
            for y in range(n-1):
                tmp = remove_possible(x,y,board)
                if tmp != None:
                    rmv_block.update(tmp)   # 지워질 블록의 좌표들 집합에 추가
        # 이번에 지워진 블록이 없다면 while문 탈출
        if not rmv_block: 
            break
            
        # 지워진 블록의 개수 answer에 추가
        answer += len(rmv_block)  
        
        # 블록 지우기
        for x,y in rmv_block:
            board[x][y] = None
         
        # 위에 있는 블록들 떨어짐
        while True:
            drop = False
            for x in range(m-2,-1,-1):
                for y in range(n):
                    if board[x][y] and board[x+1][y] == None:
                        board[x+1][y] = board[x][y]
                        board[x][y] = None
                        drop = True
            if not drop:
                break
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# 14
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
# 15