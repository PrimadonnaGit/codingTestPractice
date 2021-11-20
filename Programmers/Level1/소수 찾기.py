# https://programmers.co.kr/learn/courses/30/lessons/12921
def isPrimeNumber(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if isPrimeNumber(i):
            answer += 1
    return answer


if __name__ == '__main__':
    # n은 2이상 1,000,000이하의 자연수입니다.
    # O(n) 가능
    n = 10
    assert solution(n) == 4

    n = 5
    assert solution(n) == 3
