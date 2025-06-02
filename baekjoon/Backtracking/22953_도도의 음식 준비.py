n, k, c = map(int, input().split())
cooking_times = list(map(int, input().split()))

INF = int(1e12)
answer = INF


def total_cooking_time(arr, k):
    result = INF
    l, r = 1, INF
    while l <= r:
        mid = (l+r)//2

        count = 0
        for a in arr:
            count += mid//a
        if count < k:
            l = mid+1
        else:
            r = mid-1
            result = mid
    return result


def bt(idx, c):
    global answer
    if idx == n:
        answer = min(answer, total_cooking_time(cooking_times, k))
        return

    bt(idx+1, c)

    for encouragement in range(1, min(c+1, cooking_times[idx])):
        cooking_times[idx] -= encouragement
        bt(idx+1, c-encouragement)
        cooking_times[idx] += encouragement


cooking_times.sort()
start = 0
while start < n and cooking_times[start] == 1:
    start += 1
bt(start, c)
print(answer)
