# https://programmers.co.kr/learn/courses/30/lessons/17686
import re


def solution(files):
    # number sort
    files = sorted(files, key=lambda file: int(re.findall('\d{1,5}', file)[0]))
    # head sort
    files = sorted(files, key=lambda file: re.split('\d{1,5}', file.lower())[0])
    return files


if __name__ == '__main__':
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    assert solution(files) == ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

    files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
    assert solution(files) == ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

    files = ["img000012345", "img1.png", "img2", "IMG02"]
    assert solution(files) == ["img000012345", "img1.png", "img2", "IMG02"]
