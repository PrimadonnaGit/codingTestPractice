# https://programmers.co.kr/learn/courses/30/lessons/42891
import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 뺀다. 우선순위 큐
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식 개수

    # sum_value + (현재 음식 시간 - 이전 음식 시간) * 이전 음식 개수 와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1  # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중 몇 번째 음식인지 확인
    result = sorted(q, key=lambda x: x[1])  # 번호 기준 정렬
    return result[(k - sum_value) % length][1]


if __name__ == '__main__':
    #
    food_times, k = [3, 1, 2], 5
    assert solution(food_times, k) == 1
