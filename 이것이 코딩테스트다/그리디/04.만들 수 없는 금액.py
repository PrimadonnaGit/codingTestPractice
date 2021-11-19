def solution(n, coins):
    coins.sort()
    # target 1 부터
    target = 1
    for coin in coins:
        if target < coin:  # 타겟보다 새로운 코인이 더 큰 경우 해당 타겟을 만들 수 없다.
            break
        target += coin  # 만들어진 타겟 이하의 숫자는 모두 만들 수 있다.
    return target


if __name__ == '__main__':
    # 동전 개수 n, 1<=n<=1,000
    # n개의 동전 화폐단위, 화폐 단위 <= 1,000,000
    # n개의 동전을 이용해 만들 수 없는 양의 정수 금액의 최솟값
    n, coins = 5, [1, 1, 2, 3, 9]  # 1, 2, 4, 7, 8!
    assert solution(n, coins) == 8
    n, coins = 3, [3, 5, 7]  # # 1!
    assert solution(n, coins) == 1
