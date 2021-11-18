import math


def solution(arr):
    answer = arr[0]
    # lcd = (x*y) / gcd(x,y)
    for num in arr:
        answer = answer * num // math.gcd(answer, num)
    return answer


if __name__ == '__main__':
    arr = [2, 6, 8, 14]

    print(solution(arr))

    arr = [1, 2, 3]
    print(solution(arr))
