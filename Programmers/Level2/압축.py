# https://programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    answer = []
    dictionary = {chr(ord('A') + i - 1): i for i in range(1, 27)}

    last_index = 27
    tmp = ''
    for s in msg:
        if tmp + s not in dictionary:
            answer.append(dictionary[tmp])
            dictionary[tmp + s] = last_index
            last_index += 1
            tmp = ''
        tmp += s

    if tmp:
        answer.append(dictionary[tmp])

    return answer


if __name__ == '__main__':
    msg = 'KAKAO'
    assert solution(msg) == [11, 1, 27, 15]
    msg = 'TOBEORNOTTOBEORTOBEORNOT'
    assert solution(msg) == [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
    msg = 'ABABABABABABABAB'
    assert solution(msg) == [1, 2, 27, 29, 28, 31, 30]
