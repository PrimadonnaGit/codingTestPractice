# https://programmers.co.kr/learn/courses/30/lessons/42746
import functools


def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))


def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer


if __name__ == '__main__':
    numbers = [6, 10, 2]
    r = solution(numbers)
    print(r)
    numbers = [3, 30, 34, 5, 9]
    r = solution(numbers)
    print(r)
