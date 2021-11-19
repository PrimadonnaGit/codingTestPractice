def solution(n):
    n = str(n)
    return "LUCKY" if sum(map(int, n[:len(n) // 2])) == sum(map(int, n[len(n) // 2:])) else "READY"


if __name__ == '__main__':
    # 현재 캐릭터의 점수 N, 10 <= N <= 99,999,999, N의 자리수는 항상 짝수
    # 자리수를 기준 점수 N을 반으로 나누어 왼쪽 자리수의 합 == 오른쪽 자리수의 합
    # 같으면 LUCKY, 아니면 READY
    n = 123402
    assert solution(n) == "LUCKY"
    n = 7755
    assert solution(n) == "READY"
