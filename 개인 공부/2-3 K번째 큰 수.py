n, k = map(int, input().split())
cards = list(map(int, input().split()))

set_cards = set(cards) # 중복 제거
list_cards = list(set_cards)
list_cards.sort(reverse=True)
print(list_cards[k-1])