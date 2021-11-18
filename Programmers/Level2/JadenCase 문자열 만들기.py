# https://programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i] = s[i].capitalize()
    answer = ' '.join(s)
    return answer


if __name__ == '__main__':
    s = " a 22ab ba afw2"
    print(solution(s))
    s = "for the last week"
    print(solution(s))
