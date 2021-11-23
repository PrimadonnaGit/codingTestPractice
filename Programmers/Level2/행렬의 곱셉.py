# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = [len(arr2[0]) * [0] for _ in range(len(arr1))]
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            for k in range(len(arr1[i])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer


if __name__ == '__main__':
    arr1, arr2 = [[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]
    assert solution(arr1, arr2) == [[15, 15], [15, 15], [15, 15]]
    arr1, arr2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    assert solution(arr1, arr2) == [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
