# https://programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    command = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    road = set()
    x, y = (0, 0)

    for d in dirs:
        next_x, next_y = x + command[d][0], y + command[d][1]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            road.add((x, y, next_x, next_y))
            road.add((next_x, next_y, x, y))
            x, y = next_x, next_y

    return len(road) // 2


if __name__ == '__main__':
    dirs = "ULURRDLLU"
    print(solution(dirs))
    dirs = "LULLLLLLU"
    print(solution(dirs))
