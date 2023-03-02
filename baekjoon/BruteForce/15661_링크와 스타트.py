############# 완전탐색(PyPy3로만 통과) ################
# from itertools import combinations

# def ability_sum(team):
#     res = 0
#     team = list(team)
#     for i in range(len(team)):
#         for j in range(i+1, len(team)):
#             res += ability[team[i]-1][team[j]-1]
#             res += ability[team[j]-1][team[i]-1]
#     return res

# n = int(input())
# ability = []
# for _ in range(n):
#     ability.append(list(map(int, input().split())))
# people = set([i for i in range(1, n+1)])

# ans = 10000
# for i in range(1, n//2+1):
#     for start in combinations(people, i):
#         link = people - set(start)
#         ans = min(ans, abs(ability_sum(start)-ability_sum(link)))

# print(ans)
############### DFS ##############
# n = int(input())
# ability = []
# for _ in range(n):
#     ability.append(list(map(int, input().split())))
# people = set([i for i in range(1, n+1)])

# checked_start = set()
# ans = 1000000

# def ability_sum(team):
#     res = 0
#     team = list(team)
#     for i in range(len(team)):
#         for j in range(i+1, len(team)):
#             res += ability[team[i]-1][team[j]-1]
#             res += ability[team[j]-1][team[i]-1]
#     return res

# def dfs(start):
#     global ans
#     if len(start) == n//2+1 or tuple(start) in checked_start:
#         return
#     link = people-start
#     ans = min(ans, abs(ability_sum(start)-ability_sum(link)))
#     for i in range(1, n//2+1):
#         if i not in start:
#             start.add(i)
#             dfs(start)
#             start.remove(i)
            
# for i in range(1, n+1):
#     dfs(set([i]))

# print(ans)
###############################################################
n = int(input())
ability = []
for _ in range(n):
    ability.append(list(map(int, input().split())))
people = set([i for i in range(1, n+1)])
checked = [False] * (2 ** (n+1))

ans = 1000000
def get_diff(num):
    start, link = [], []
    start_sum, link_sum = 0, 0
    for i in range(1, n+1):
        if num % 2 == 1:  # 스타트팀 멤버
            start.append(i)
            for member in start:
                start_sum += ability[i-1][member-1]
                start_sum += ability[member-1][i-1]
        else:
            link.append(i)
            for member in link:
                link_sum += ability[i-1][member-1]
                link_sum += ability[member-1][i-1]
        num //= 2
    # print("start:", *start, "link:", *link)
    return abs(start_sum-link_sum)

def dfs(team, num): # 팀구성(비트마스킹), 현재 보고 있는 사람 번호(0 ~ N-1번)
    global ans
    if not checked[team]:
        ans = min(ans, get_diff(team))
        checked[team] = True
    if num < n :
        dfs(team, num+1)
        team |= (1 << num+1)
        dfs(team, num+1)

for i in range(n):
    dfs(1 << i, i)
print(ans)