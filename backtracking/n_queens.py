def solveNQueens(n):
    result = []
    current = [["."] * n for r in range(n)]

    cols = []
    posDiag = []
    negDiag = []

    def is_a_solution(k):
        return k == n

    def process_solution():
        result.append(["".join(c) for c in current])

    def construct_candidates(k):
        return [c for c in range(n) if c not in cols and (c + k) not in posDiag and (c - k) not in negDiag]

    def make_move(k, c):
        current[k][c] = 'Q'
        cols.append(c)
        posDiag.append(c+k)
        negDiag.append(c-k)

    def unmake_move(k, c):
        current[k][c] = '.'
        cols.pop()
        posDiag.pop()
        negDiag.pop()

    def backtrack(k):
        if is_a_solution(k):
            process_solution()
        else:
            candidates = construct_candidates(k)
            for c in candidates:
                make_move(k, c)
                backtrack(k + 1)
                unmake_move(k, c)

    backtrack(0)

    return result
