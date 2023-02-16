# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# for i in sorted(a + b):
#     print(i, end=' ')
    
#######################################
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# arr = a + b

# def quickSort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot, tail = arr[0], arr[1:]
    
#     left = [x for x in tail if x <= pivot]
#     right = [x for x in tail if x > pivot]
    
#     return quickSort(left) + [pivot] + quickSort(right)

# for i in quickSort(arr):
#     print(i, end=' ')

############ 정렬되어 있는 두 배열 합치기 ############
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p1 = p2 = 0

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        print(a[p1], end=' ')
        p1 += 1
    else:
        print(b[p2], end=' ')
        p2 += 1
        
if p1 < n:
    print(*a[p1:])
if p2 < m:
    print(*b[p2:])