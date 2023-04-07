from itertools import combinations
def get_score(nums, scores):
    # 그룹으로 나누기
    nums = sorted(nums)
    group = [[nums[0]]]
    res = scores[nums[0]]
    for i in nums[1:]:
        if i-1 == group[-1][-1]:
            group[-1].append(i)
        else:
            group.append([i])
        res += scores[i]
    # 그룹 크기별 추가 점수 부여
    for j in group:
        if len(j) == 4:
            res += 5
        elif len(j) == 3:
            res += 3
        elif len(j) == 2:
            res += 2
    return res

def solution(scores):
    answer = 0
    for nums in combinations(range(len(scores)), 4):
        answer = max(answer, get_score(list(nums), scores))
    return answer