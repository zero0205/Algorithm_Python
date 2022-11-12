from itertools import combinations
# 좌우 개수 차이 적게, 구슬 개수 사용은 많게, 무게는 무겁게, 배열에 담으면 사전순으로 빠른 거

# 무게가 같은 2개의 묶음으로 나누기 가능?
def divide(arr):
    if sum(arr) % 2 == 1:
        return None
    half = len(arr) // 2
    for i in range(half, 0, -1):
        for lst in sorted(list(combinations(arr, i))):
            if sum(lst) == (sum(arr) // 2):
                return [arr, list(lst)] # 원배열과 왼쪽 리턴
    return None # 나눌 수 없는 경우

def make_lst(left, center, original):
    if center == -1:    # 센터 없음
        for el in left:
            original.remove(el)
        return left + original
    else:   # 센터 있음
        for el in left:
            original.remove(el)
        return left + [center] + original
# 장식 만들 수 있는가
def possible(arr):  
    if len(arr) == 1:
        return [arr, 0]
    min_gap = 10
    ans = []
    arr.sort() # 사전 순 고려
    if len(arr) % 2 == 1:   # 홀수 개
        for i in range(len(arr), -1, -1):
            res = divide(arr[:i]+arr[i+1:])
            if res == None:
                continue
            original, lst = res
            gap = abs(len(original) - 2 * len(lst))
            if gap == 0:    # 양쪽 개수 차이가 0보다 작을 수는 없음
                return [make_lst(lst, arr[i], original), gap]
            if gap < min_gap:
                min_gap = gap
                ans = make_lst(lst, -1, original)
        return [ans, min_gap]
    else:   # 짝수 개
        res = divide(arr)
        for i in range(len(arr), 1, -1):
            if res == None:
                continue
            original, lst = res
            gap = abs(len(original) - 2 * len(lst))
            if gap == 0:
                return [make_lst(lst, -1, original), gap]
            if gap < min_gap:
                min_gap = gap
                ans = make_lst(lst, -1, original)
        return [ans, min_gap]

def solution(marbles):
    answer = []
    min_gap = 10
    n = len(marbles)
    marbles.sort(reverse=True)  # 개수가 같다면 무거운 애들부터 고르도록
    for i in range(n, 0, -1):
        for lst in sorted(list(combinations(marbles, i)), reverse=True):
            res, gap = possible(list(lst))
            if gap < min_gap:
                answer = res
                min_gap = gap
    return answer


print(solution([1,2,3,4,4]))
# [1,4,4,2,3]
print(solution([5,5,1,4]))
# [5,4,5]
print(solution([3,9,7,5]))
# [3,9,5,7]
print(solution([7,3,1]))
# [7]