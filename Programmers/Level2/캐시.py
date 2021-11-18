# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)

    cache_hit = 1
    cache_miss = 5
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += cache_hit
            cache.remove(city)
        else:
            answer += cache_miss
        cache.append(city)

    return answer


if __name__ == '__main__':
    cacheSize, cities = 3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(solution(cacheSize, cities))
    cacheSize, cities = 3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
    print(solution(cacheSize, cities))
    cacheSize, cities = 2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris",
                            "Jeju", "NewYork", "Rome"]
    print(solution(cacheSize, cities))
    cacheSize, cities = 5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris",
                            "Jeju", "NewYork", "Rome"]
    print(solution(cacheSize, cities))
    cacheSize, cities = 2, ["Jeju", "Pangyo", "NewYork", "newyork"]
    print(solution(cacheSize, cities))
    cacheSize, cities = 0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(solution(cacheSize, cities))
