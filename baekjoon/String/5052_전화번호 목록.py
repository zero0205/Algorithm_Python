import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    phones = [input().rstrip() for _ in range(n)]

    phones.sort()
    possible = True
    for i in range(len(phones)-1):
        if phones[i] == phones[i+1][:len(phones[i])]:
            possible = False
            break
    print("YES" if possible else "NO")
