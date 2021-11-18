# https://programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    answer = []
    board = [list(range(i * columns + 1, (i + 1) * columns + 1)) for i in range(rows)]
    for query in queries:
        query = [x - 1 for x in query]  # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = board[query[0]][query[1]]  # 왼쪽 위 값 저장
        small = tmp

        # left
        for i in range(query[0] + 1, query[2] + 1):
            board[i - 1][query[1]] = board[i][query[1]]
            small = min(small, board[i][query[1]])
        # bottom
        for i in range(query[1] + 1, query[3] + 1):
            board[query[2]][i - 1] = board[query[2]][i]
            small = min(small, board[query[2]][i])
        # right
        for i in range(query[2] - 1, query[0] - 1, -1):
            board[i + 1][query[3]] = board[i][query[3]]
            small = min(small, board[i][query[3]])
        # top
        for i in range(query[3] - 1, query[1] - 1, -1):
            board[query[0]][i + 1] = board[query[0]][i]
            small = min(small, board[query[0]][i])
        board[query[0]][query[1] + 1] = tmp

        answer.append(small)

    return answer


if __name__ == '__main__':
    rows, columns, queries = 6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
    r = solution(rows, columns, queries)
    print(r)
    rows, columns, queries = 3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
    r = solution(rows, columns, queries)
    print(r)
    rows, columns, queries = 100, 97, [[1, 1, 100, 97]]
    r = solution(rows, columns, queries)
    print(r)
