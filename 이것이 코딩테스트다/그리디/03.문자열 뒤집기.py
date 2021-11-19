def solution(s):
    # 모두 0으로 바꾸는 경우, 모두 1로 바꾸는 경우를 따진 후 적은 것을 반환
    count0 = 0
    count1 = 0

    if s[0] == '1':
        count0 += 1
    else:
        count1 += 1

    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:  # 0->1 , 1->0
            if s[i + 1] == '1':
                count0 += 1
            else:
                count1 += 1

    return min(count0, count1)


if __name__ == '__main__':
    # 0,1로 이루어진 문자열 s, len(s) <= 1,000,000
    # s의 모든 숫자를 같도록 연속된 하나 이상의 숫자를 모두 뒤집는(0<->1) 행동
    # 행동의 최소 횟수
    s = '0001100'
    assert solution(s) == 1
