# https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for a1, b1 in zip(A, B):
        answer += a1 * b1
    return answer


if __name__ == '__main__':
    a, b = [1, 4, 2], [5, 4, 4]
    assert solution(a, b) == 29
    a, b = [1, 2], [3, 4]
    assert solution(a, b) == 10
