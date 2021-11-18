# https://programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    answer = True
    left_count = 0
    right_count = 0
    for c in s:
        if c == '(':
            left_count += 1
        else:
            right_count += 1

        if right_count > left_count:
            return False
    if left_count != right_count:
        return False
    return True


if __name__ == '__main__':
    s = "()()"
    assert solution(s) == True
    s = "(())()"
    assert solution(s) == True
    s = ")()("
    assert solution(s) == False
    s = "(()("
    assert solution(s) == False
