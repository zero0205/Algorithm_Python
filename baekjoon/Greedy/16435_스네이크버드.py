def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less, equal, greater = [], [], []
    for a in arr:
        if a < pivot:
            less.append(a)
        elif a == pivot:
            equal.append(a)
        else:
            greater.append(a)
    return quick_sort(less)+equal+quick_sort(greater)


n, l = map(int, input().split())
h = list(map(int, input().split()))

h = quick_sort(h)

for i in range(n):
    if l < h[i]:
        break
    l += 1

print(l)
