# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    min_num = min(map(int, s.split()))
    max_num = max(map(int, s.split()))
    return f'{min_num} {max_num}'


if __name__ == '__main__':
    s = "1 2 3 4"
    assert solution(s) == "1 4"
    s = "-1 -2 -3 -4"
    assert solution(s) == "-4 -1"
    s = "-1 -1"
    assert solution(s) == "-1 -1"
