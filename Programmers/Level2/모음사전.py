# https://programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product


def solution(word):
    pivot = 'AEIOU'
    dictionary = []
    for i in range(1, len(pivot) + 1):
        dictionary += [''.join(w) for w in product(pivot, repeat=i)]

    dictionary.sort()
    return dictionary.index(word) + 1


if __name__ == '__main__':
    word = "AAAAE"
    print(solution(word))
    word = "AAAE"
    print(solution(word))
    word = "I"
    print(solution(word))
    word = "EIO"
    print(solution(word))
