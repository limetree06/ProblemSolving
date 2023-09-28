import sys

""" 
 Anagram 유명한 문제
 풀이방법
 1. 딕셔너리 해쉬
 1-1. 리스트 해쉬
 
 """


def set_dict(words):
    ana = dict()
    for word in words:
        if word in ana:
            ana[word] += 1
        else:
            ana[word] = 0
    return ana


def compare(ana1, ana2):
    for key in ana1.keys():
        if ana1[key] != ana2[key]:
            return "NO"
    else:
        return "YES"


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    ana1 = set_dict(list(input()))
    ana2 = set_dict(list(input()))

    print(compare(ana1, ana2))
