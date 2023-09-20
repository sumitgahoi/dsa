def subsets(input):
    result = []
    current = [None] * len(input)

    def is_a_solution(k):
        return k == len(input)

    def process_solution():
        r = [input[i] for i in range(len(current)) if current[i]]
        result.append(r)

    def construct_candidates(k):
        return [True, False]

    def make_move(k, c):
        current[k] = c

    def unmake_move(k):
        current[k] = None

    def backtrack(k):
        if is_a_solution(k):
            process_solution()
        else:
            candidates = construct_candidates(k)
            for c in candidates:
                make_move(k, c)
                backtrack(k + 1)
                unmake_move(k)

    backtrack(0)

    return result
