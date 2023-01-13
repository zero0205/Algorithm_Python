# 누르려는 번호에서부터 가까운 손가락 리턴
def check_dist(location, l, r):
    l_dist = abs(location[0] - l[0]) + abs(location[1] - l[1])
    r_dist = abs(location[0] - r[0]) + abs(location[1] - r[1])
    
    if l_dist == r_dist:
        return 's'
    elif l_dist > r_dist:
        return 'r'
    else: 
        return 'l'

def solution(numbers, hand):
    answer = ''
    l = (3,0)   # 처음 왼손 위치
    r = (3,2)   # 처음 오른손 위치
    
    location = {1:(0,0), 2:(0,1), 3:(0,2),
                4:(1,0), 5:(1,1), 6:(1,2),
                7:(2,0), 8:(2,1), 9:(2,2), 
                0:(3,1)}
    
    for n in numbers:
        if n in (1,4,7):    # 왼손으로 누를 경우
            answer += 'L'
            l = location[n]
            continue
        elif n in (3, 6, 9):   # 오른손으로 누를 경우
            answer += 'R'
            r = location[n]
            continue
        else:   # 가운데 키패드인 경우
            if check_dist(location[n], l, r) == 's':    # 거리가 같은 경우
                if hand == "left":
                    answer += 'L'
                    l = location[n]
                    continue
                else:
                    answer += 'R'
                    r = location[n]
                    continue
            elif check_dist(location[n], l, r) == 'l':
                answer += 'L'
                l = location[n]
                continue
            else:
                answer += 'R'
                r = location[n]
                continue
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# LRLLLRLLRRL
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# LRLLRRLLLRR
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	, "right"))
# LLRLLRLLRL