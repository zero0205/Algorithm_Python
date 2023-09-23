from collections import defaultdict
import sys
input = sys.stdin.readline


def bt(w, length, visited):
    if len(w) == length:
        print("".join(w))
        return
    for a in alphabet:
        if alphabet[a]:
            visited[a] -= 1
            bt(w+a, length, visited)
            visited[a] += 1


for _ in range(int(input())):
    word = sorted(list(input().strip()))
    alphabet = defaultdict(int)
    for w in word:
        alphabet[w] += 1
    bt('', len(word), alphabet)
