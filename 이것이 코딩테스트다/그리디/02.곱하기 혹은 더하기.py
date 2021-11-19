def solution(s):
    # 현재까지의 값과 현재 들어오는 값이 0,1이 아닌 이상 곱하는 것이 무조건 이득
    result = 0
    for i in s:
        if int(i) <= 1 or result <= 0:
            result += int(i)
        else:
            result *= int(i)
    return result


if __name__ == '__main__':
    # 각 자리가 숫자(0~9), 숫자 사이에 + 혹은 *
    # 결과적으로 가장 큰 수, 계산은 무조건 원쪽부터
    s = '02984'
    assert solution(s) == 576

    s = '567'
    assert solution(s) == 210
