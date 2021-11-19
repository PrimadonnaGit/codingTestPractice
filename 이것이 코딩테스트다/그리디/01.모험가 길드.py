def solution(n, fear):
    # 공포도가 낮은 순서대로 그룹에 포함
    fear.sort()
    # 공포도가 오름차순으로 정렬되어 있기 때문에 현재 모험가의 공포도만 조사하면 최소한의 인원으로 그룹을 만들 수 있다.
    # 따라서, 최대한의 그룹을 만들 수 있다.

    group_count = 0
    group_member = 0
    for i in fear:
        group_member += 1
        if group_member >= i:  # 그룹에 포함된 멤버의 수가 들어오려는 멤버의 공포도 보다 높거나 같다면
            group_count += 1
            group_member = 0  # 그룹 초기화

    return group_count  # [1], [2,2], 2,3


if __name__ == '__main__':
    # 모험가수 N, 1 <= N <= 100,000
    # 공포도는 N이하의 자연수, 모든 모험가가 그룹에 들어갈 필요는 없음
    n, fear = 5, [2, 3, 1, 2, 2]
    assert solution(n, fear) == 2
