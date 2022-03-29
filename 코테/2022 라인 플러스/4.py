# arr[i] != brr[i]라면 arr은 최소 1번은 움직여야 함
def solution(arr, brr):
    answer = 0
    for idx in range(len(arr) - 1):
        if arr[idx] == brr[idx]:
            continue
        elif arr[idx] > brr[idx]:
            arr[idx + 1] += (arr[idx] - brr[idx])
            arr[idx] = brr[idx]
            answer += 1
        else:
            arr[idx + 1] -= (brr[idx] - arr[idx])
            arr[idx] = brr[idx]
            answer += 1
    return answer

print(solution([3, 7, 2, 4], [4, 5, 5, 2]))
print(solution([6, 2, 2, 6], [4, 4, 4, 4]))