from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

post_order = []
while True:
    try:
        post_order.append(int(input()))
    except:
        break
    
def pre_order(start, end, ans):
    if start > end:
        return

    idx = start + 1
    
    # 이전보다 작아지는 지점을 찾기 -> 그 지점이 루트
    while idx <= end:
        if post_order[idx] < post_order[idx-1]:
            break
        idx += 1
    for i in range(start, idx):
        ans.append(post_order[i])
    pre_order(idx, len(post_order) -1, ans)   # 위로
    return ans

ans = []
for i in pre_order(0, len(post_order) - 1, ans):
    print(i)