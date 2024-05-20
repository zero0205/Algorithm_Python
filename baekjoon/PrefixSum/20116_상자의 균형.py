n, l = map(int, input().split())
x = list(map(int, input().split()))

center = x[-1]  # 무게 중심
num = 1
for i in range(n-2, -1, -1):
    if center <= (x[i]-l) or center >= (x[i]+l):
        print("unstable")
        exit()
    center = ((center*num)+x[i])/(num+1)    # 위에서부터 i번째까지의 무게 중심
    num += 1    # i번째까지 상자 개수

print("stable")
