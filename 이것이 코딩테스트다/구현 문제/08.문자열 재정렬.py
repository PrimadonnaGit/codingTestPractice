def solution(s):
    digit_sum = 0
    tmp = []
    for char in s:
        if char.isalpha():
            tmp.append(char)
        else:
            digit_sum += int(char)

    tmp.sort()
    if digit_sum:
        tmp.append(str(digit_sum))

    return ''.join(tmp)


if __name__ == '__main__':
    # 알파벳 대문자와 0~9로만 이루어진 문자열 s, 1<= len(s) <= 10,000
    # 알파벳을 오름차순으로 정렬 후 모든 숫자를 더한 값을 이어서 출력
    s = 'K1KA5CB7'
    assert solution(s) == 'ABCKK13'
    s = 'AJKDLSI412K4JSJ9D'
    assert solution(s) == 'ADDIJJJKKLSS20'
