# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution(jobs):
    answer = 0
    current = 0
    i = 0
    start = -1
    waiting = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= current:
                heapq.heappush(waiting, j[::-1])

        if len(waiting) > 0:
            processing = heapq.heappop(waiting)
            start = current
            current += processing[0]
            answer += (current - processing[1])
            i += 1
        else:
            current += 1

    return int(answer / len(jobs))


if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]
    assert solution(jobs) == 9
