import sys
input = sys.stdin.readline

voca = input().rstrip()
required = [0] * 26 
# 필요한 알파벳 개수 카운트
for v in voca:
    required[ord(v)-65] += 1

n = int(input())
books = []
for i in range(n):
    cost, title = input().split()  # 가격, 제목
    books.append([title, int(cost)])
 
ans = int(1e9)
selected = [0] * 26 # 선택된 책들의 알파벳

def dfs(idx, total_cost):
    global ans
    if idx == len(books):
        # 만들 수 있는지 확인
        for i in range(26):
            if required[i] > selected[i]:
                return
        ans = min(ans, total_cost)
        return
    # 현재 책 선택 O
    for c in books[idx][0]: # c는 현재 책의 제목 글자 하나
        selected[ord(c)-65] += 1    
    dfs(idx+1, total_cost + books[idx][1])
    # 현재 책 선택 X
    for c in books[idx][0]: # c는 현재 책의 제목 글자 하나
        selected[ord(c)-65] -= 1
    dfs(idx+1, total_cost)
    
dfs(0, 0)
print(ans if ans != int(1e9) else -1)