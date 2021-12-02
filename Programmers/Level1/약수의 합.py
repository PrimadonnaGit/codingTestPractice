# https://programmers.co.kr/learn/courses/30/lessons/12928
def get_divisor(n):
    divisors = []
    for i in range(1, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            divisors.append(i)
            if i ** 2 != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def solution(n):
    return sum(get_divisor(n))


if __name__ == '__main__':
    # n은 0 이상 3000이하인 정수입니다.
    n = 12
    assert solution(n) == 28

    n = 5
    assert solution(n) == 6
