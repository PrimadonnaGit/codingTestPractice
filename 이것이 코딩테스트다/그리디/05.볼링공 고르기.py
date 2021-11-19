def solution(n, m, k):
    k.sort()
    # 작은 숫자부터 숫자가 같지 않은 것들의 개수를 합하는 방식
    count = 0
    for i in range(n):
        count += len([j for j in k[i + 1:] if j != k[i]])
    return count


if __name__ == '__main__':
    # 두 사람이 서로 무게가 다른 볼링공을 고르는 경우의 수
    # 볼링공 개수 n, 같은 무게가 있을 수 있지만 서로 다른 공, 1<=n<=1,000
    # 볼링공 무게 m (1~m) , 1<=m<=10
    n, m, k = 5, 3, [1, 3, 2, 3, 2]
    assert solution(n, m, k) == 8
    n, m, k = 8, 5, [1, 5, 4, 3, 2, 4, 5, 2]
    assert solution(n, m, k) == 25
