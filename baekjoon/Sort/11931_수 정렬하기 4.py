import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr

    left = merge_sort(arr[:n//2])
    right = merge_sort(arr[n//2:])

    l_idx, r_idx = 0, 0
    result = []
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] > right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1

    while l_idx < len(left):
        result.append(left[l_idx])
        l_idx += 1

    while r_idx < len(right):
        result.append(right[r_idx])
        r_idx += 1
    return result


def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n//2]

    left = []
    right = []
    for i in range(n):
        if i == n//2:
            continue
        if arr[i] > pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left)+[pivot]+quick_sort(right)


def heapify(arr, n, root):
    smallest = root
    left_child = root*2+1
    right_child = root*2+2

    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child
    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child

    if smallest != root:
        arr[smallest], arr[root] = arr[root], arr[smallest]
        heapify(arr, n, smallest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


# print(*merge_sort(arr), sep="\n")
# print(*quick_sort(arr), sep="\n")
print(*heap_sort(arr), sep="\n")
