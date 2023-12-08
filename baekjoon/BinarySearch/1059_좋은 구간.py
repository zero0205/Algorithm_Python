l = int(input())
arr = list(map(int, input().split()))
n = int(input())

arr = sorted(arr)
s, e = 0, l-1
left = -1
while s <= e:
    mid = (s+e)//2
    if arr[mid] == n:
        print(0)
        exit()
    elif arr[mid] < n:
        left = mid
        s = mid+1
    else:
        e = mid-1
if left == -1:
    ans = (n-1)*(arr[0]-n)+(arr[0]-n-1)
else:
    ans = (n-arr[left]-1)*(arr[left+1]-n)+(arr[left+1]-n-1)
print(ans)
