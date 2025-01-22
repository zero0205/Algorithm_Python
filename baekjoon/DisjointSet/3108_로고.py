import sys
input = sys.stdin.readline


class Square:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def meet(self, square):
        if self.x1 < square.x1 and self.y1 < square.y1 and self.x2 > square.x2 and self.y2 > square.y2:
            return False
        if self.x1 > square.x1 and self.y1 > square.y1 and self.x2 < square.x2 and self.y2 < square.y2:
            return False
        if self.x1 > square.x2 or self.y2 < square.y1 or self.x2 < square.x1 or self.y1 > square.y2:
            return False
        return True


n = int(input())
squares = []
parent = [i for i in range(n+1)]
squares.append(Square(0, 0, 0, 0))


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    squares.append(Square(x1, y1, x2, y2))

for i in range(n+1):
    for j in range(i+1, n+1):
        if (squares[i].meet(squares[j])):
            union(i, j)

for i in range(n+1):
    parent[i] = find_parent(i)

print(len(set(parent))-1)
