import sys
input = sys.stdin.readline

n = int(input())
arr = [0]+list(map(int, input().split()))
open = [True]*(n+1)
q = int(input())
sum_water = sum(arr)
print(sum_water)
for _ in range(q):
    line = list(map(int, input().split()))
    if line[0] == 1:
        if open[line[1]]:
            sum_water += (line[2]-arr[line[1]])
        arr[line[1]] = line[2]
    elif line[0] == 2:
        if open[line[1]]:
            sum_water -= arr[line[1]]
        else:
            sum_water += arr[line[1]]
        open[line[1]] = not open[line[1]]
    else:
        print("Error!")
        break
    print(sum_water)