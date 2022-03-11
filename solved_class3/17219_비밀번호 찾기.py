import sys
input = sys.stdin.readline
# n : 저장된 사이트 주소의 수, m : 비밀번호를 찾으려는 사이트 주소의 수
n, m = map(int, input().split())

# 사이트 주소와 비번 입력받기
d = {}
for _ in range(n):
    addr, pw = input().rstrip().split()
    d[addr] = pw
    
# 비밀번호 찾아줘!
for _ in range(m):
    addr = input().rstrip()
    print(d[addr])