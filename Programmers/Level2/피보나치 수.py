# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    dp = [0] * 100001
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1234567


if __name__ == '__main__':
    n = 3
    assert solution(n) == 2
    n = 5
    assert solution(n) == 5
