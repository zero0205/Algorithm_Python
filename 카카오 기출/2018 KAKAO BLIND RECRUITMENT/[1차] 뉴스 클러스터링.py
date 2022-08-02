from collections import defaultdict

def split_str(str):
    res = defaultdict(int)
    str = str.upper()
    for i in range(len(str) - 1):
        tmp = str[i:i + 2]
        if tmp.isalpha():
            res[tmp] += 1
    return res

def solution(str1, str2):
    answer = 0
    s1 = split_str(str1)
    s2 = split_str(str2)
    if len(s1) == 0 and len(s2) == 0:   # 둘 다 공집합인 경우
        return 65536
    union_set = defaultdict(list)
    for k, v in s1.items():
        union_set[k].append(v)
    for k, v in s2.items():
        union_set[k].append(v)
    inter, uni = 0, 0
    for k, v in union_set.items():
        if len(v) > 1:  # 다른 문자열 집합에 아예 등장하지않은 경우 고려하기 위해
            inter += min(v)
        uni += max(v)
        
    answer = int((inter / uni) * 65536) 
    return answer

print(solution("FRANCE", "french"))
# 16384
print(solution("handshake", "shake hands"))
# 65536
print(solution("aa1+aa2", "AAAA12"))
# 43690
print(solution("E=M*C^2", "e=m*c^2"))
# 65536

###########################
def solution2(str1, str2):
    s1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    
    inter_set = set(s1) & set(s2)
    union_set = set(s1) | set(s2)
    
    if len(union_set) == 0:
        return 65536
    
    inter = sum([min(s1.count(i), s2.count(i)) for i in inter_set])
    uni = sum([max(s1.count(u), s2.count(u)) for u in union_set])
    return int((inter/uni) * 65536)

print(solution2("FRANCE", "french"))
# 16384
print(solution2("handshake", "shake hands"))
# 65536
print(solution2("aa1+aa2", "AAAA12"))
# 43690
print(solution2("E=M*C^2", "e=m*c^2"))
# 65536