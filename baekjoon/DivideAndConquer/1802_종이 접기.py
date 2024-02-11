def dc(arr):
    if len(arr) == 1:
        return True
    mid = len(arr)//2
    for i in range(mid):
        if arr[i] == arr[len(arr)-1-i]:
            return False
    return dc(arr[:mid]) and dc(arr[mid+1:])


for _ in range(int(input())):
    fold = input()
    print("YES" if dc(fold) else "NO")
