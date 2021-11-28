# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    base_count = bin(n)[2:].count('1')
    while True:
        n += 1
        if bin(n)[2:].count('1') == base_count:
            break

    return n


if __name__ == '__main__':
    n = 78
    assert solution(n) == 83

    n = 15
    assert solution(n) == 23
