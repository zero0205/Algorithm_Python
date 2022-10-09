def dfs(cards, new_cards, num, shuffles):
    if cards == new_cards:
        return num
    for i in range(len(cards)):
        if new_cards[shuffles[i]-1] != cards[i]:
            tmp = new_cards[shuffles[i]-1]
            new_cards[shuffles[i]-1] = cards[i]
            num = max(num, dfs(cards, new_cards, num + 1, shuffles))
            new_cards[shuffles[i]-1] = tmp

def solution(cards, shuffles):
    answer = -1
    new_cards = [0] * len(cards)
    dp = [0] * len(cards)
    for i in range(len(cards)):
        new_cards[shuffles[i]-1] = cards[i]

    answer = dfs(cards, new_cards, 0, shuffles)
    return answer