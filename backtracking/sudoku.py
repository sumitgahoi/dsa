from typing import List

class Sudoku:
    def solve(self, board: List[List[str]]) -> None:
        # sudoku is a 9x9 board
        rows = 9
        columns = 9

        # track filled slots
        self.filled_slots = 0

        # keep track of values already taken by each row, column and 3x3 squares
        row_values = [set() for i in range(rows)]
        col_values = [set() for i in range(columns)]
        block_values = [[set() for i in range(3)] for j in range(3)]

        # prefill with values already on board
        for i in range(rows):
            for j in range(columns):
                if board[i][j] != '.':
                    self.filled_slots += 1
                    row_values[i].add(board[i][j])
                    col_values[j].add(board[i][j])
                    block_values[i//3][j//3].add(board[i][j])

        # returns true if all slots are filled with legal values
        def is_a_solution():
            return self.filled_slots == 81

        # returns all possible legal values for the given slot
        def construct_candidates(i, j):
            return [v for v in "123456789" if v not in row_values[i] and v not in col_values[j] and v not in block_values[i//3][j//3]]

        # assign a value c to the given slot and some house-keeping
        def make_move(i, j, c):
            board[i][j] = c
            self.filled_slots += 1
            row_values[i].add(c)
            col_values[j].add(c)
            block_values[i//3][j//3].add(c)

        # revert everything that was done prior to backtracking at this slot
        def unmake_move(i, j, c):
            board[i][j] = '.'
            self.filled_slots -= 1
            row_values[i].remove(c)
            col_values[j].remove(c)
            block_values[i//3][j//3].remove(c)

        # next slot to backtrack on
        def next_pos(i, j):
            j = j + 1
            if j == columns:
                # move to next row
                return (i + 1, 0)
            else:
                # move to next colum
                return (i, j)

        def backtrack(i, j):
            # if we have a solution already, no need to do anything further
            if is_a_solution():
                return True
            # if the board already had a value, move to the next slot
            elif board[i][j] != '.':
                x, y = next_pos(i, j)
                return backtrack(x, y)
            # try all possible values for this slot
            else:
                candidate_values = construct_candidates(i, j)
                for c in candidate_values:
                    make_move(i, j, c)
                    x, y = next_pos(i, j)
                    if backtrack(x, y):
                        return True
                    unmake_move(i, j, c)
                return False

        # search for a legal solution starting at first index
        backtrack(0, 0)
