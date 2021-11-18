# https://programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    answer = []
    triangle = [[0 for j in range(1, i + 1)] for i in range(1, n + 1)]

    row, col = -1, 0  # 아래로
    num = 1
    # 하 -> 우 -> 좌 -> 하 -> 우 -> 좌
    # 0 -> 1 -> 2 -> 3 -> 4 -> 5
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:  # 하
                row += 1
            elif i % 3 == 1:  # 우
                col += 1
            else:  # 상
                row -= 1
                col -= 1
            triangle[row][col] = num
            num += 1

    return sum(triangle, [])


if __name__ == '__main__':
    n = 4
    print(solution(n))
    n = 5
    print(solution(n))
    n = 6
    print(solution(n))
