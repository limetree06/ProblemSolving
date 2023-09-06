import sys

""" 
알게된 점 : [::-1] => 카드를 역순으로 만드는 것
"""


def reverse_cards(cards, range_card):
    start = range_card[0]
    end = range_card[1]
    reverse_list = cards[start - 1 : end][::-1]

    for i in range(len(reverse_list)):
        cards[i + start - 1] = reverse_list[i]
    return cards


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    cards = [i + 1 for i in range(20)]
    input_range_list = []
    for i in range(10):
        input_range_list.append(list(map(int, input().split())))

    for range_card in input_range_list:
        cards = reverse_cards(cards, range_card)
    print(cards)
