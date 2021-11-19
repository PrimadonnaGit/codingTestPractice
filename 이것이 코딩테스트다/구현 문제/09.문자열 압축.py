# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = 1000
    for cs in range(1, len(s) // 2 + 2):
        cnt = 1
        target = s[:cs]
        result = ''

        for i in range(cs, len(s) + cs, cs):
            tmp = s[i:i + cs]
            if tmp == target:
                cnt += 1
            else:
                if cnt == 1:
                    result += target
                else:
                    result += str(cnt) + target
                cnt = 1
                target = tmp

        answer = min(answer, len(result))

    return answer


if __name__ == '__main__':
    s = "aabbaccc"
    assert solution(s) == 7
    s = "ababcdcdababcdcd"
    assert solution(s) == 9
    s = "abcabcdede"
    assert solution(s) == 8
    s = "abcabcabcabcdededededede"
    assert solution(s) == 14
    s = "xababcdcdababcdcd"
    assert solution(s) == 17
