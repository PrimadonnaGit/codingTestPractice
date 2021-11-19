from collections import deque


# 그래프에서 모든 간선의 비용이 동일할 때는 너비 우선 탐색(BFS)를 이용하여 해결
# 모든 도시까지의 최단거리를 구하고, 그 값이 K인 경우 출력 O(N+M)
def solution(n, m, k, x, roads):
    graph = [[] for _ in range(n + 1)]

    for a, b in roads:
        graph[a].append(b)

    # 모든 도시에 대한 최단 거리 초기화
    distance = [-1] * (n + 1)
    distance[x] = 0

    # BFS
    q = deque([x])
    while q:
        now = q.popleft()
        # now 도시에서 이동할 수 있는 모든 도시 확인
        for next_node in graph[now]:
            # 아직 방문하지 않은 곳
            if distance[next_node] == -1:
                # 최단 거리 갱신
                distance[next_node] = distance[now] + 1
                q.append(next_node)

    # 최단 거리가 K인 모든 도시 번호를 오름차순으로 출력
    k_list = [i for i, d in enumerate(distance) if d == k]
    k_list.sort()
    return k_list if k_list else [-1]


if __name__ == '__main__':
    # n개 도시, m개 단방향 도로, 최단거리 k, 출발도시 x
    n, m, k, x = 4, 4, 2, 1
    roads = [[1, 2], [1, 3], [2, 3], [2, 4]]
    assert solution(n, m, k, x, roads) == [4]

    n, m, k, x = 4, 3, 2, 1
    roads = [[1, 2], [1, 3], [1, 4]]
    assert solution(n, m, k, x, roads) == [-1]

    n, m, k, x = 4, 4, 1, 1
    roads = [[1, 2], [1, 3], [2, 3], [2, 4]]
    assert solution(n, m, k, x, roads) == [2, 3]