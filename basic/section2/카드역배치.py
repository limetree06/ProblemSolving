import sys

""" 
알게된 점 : [::-1] => 카드를 역순으로 만드는 것

나의 풀이 : 역으로 만든 리스트를 만들어서 그 위에 가져다가 붙이는 방법으로 품
조금더 효율적인 풀이 : reverse해야하는 카드를 바꿔야하는 부분끼리 바꾼다. 1, 2, 3, 4, 5 => 1과 5바꾸고 2와 4바꾸고
    a, b = b, a (이렇게 swap할 수 있다.)
"""


# def reverse_cards(cards, range_card):
#     start = range_card[0]
#     end = range_card[1]
#     reverse_list = cards[start - 1 : end][::-1]

#     for i in range(len(reverse_list)):
#         cards[i + start - 1] = reverse_list[i]
#     return cards


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
