# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        sum = 0
        while sum < n:
            sum += i
            i += 1
        if sum == n:
            answer += 1
    return answer


if __name__ == '__main__':
    n = 15
    assert solution(n) == 4
