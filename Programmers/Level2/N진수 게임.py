# https://programmers.co.kr/learn/courses/30/lessons/17687

def convert(num, base):
    tmp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    # n진법, t개 예측, m 전체 인원, 튜브의 순서 p
    answer = ''
    tmp = ''
    for i in range(m * t):
        tmp += str(convert(i, n))

    while len(answer) < t:
        answer += tmp[p - 1]
        p += m

    return answer


if __name__ == '__main__':
    n, t, m, p = 2, 4, 2, 1
    assert solution(n, t, m, p) == "0111"
    n, t, m, p = 16, 16, 2, 1
    assert solution(n, t, m, p) == "02468ACE11111111"
    n, t, m, p = 16, 16, 2, 2
    assert solution(n, t, m, p) == "13579BDF01234567"
