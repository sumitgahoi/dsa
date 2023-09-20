def generic_backtracking(input):
    result = []
    current = []
    
    def is_a_solution(k):
        return False
    
    def process_solution():
        result.append(list(current))

    def construct_candidates(k):
        return []
    
    def make_move(k, c):
        return
    
    def unmake_move(k):
        return

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