from maths.gcd import gcd
from maths.prime import is_prime, generate_pseudo_random
from maths.expand import expand, modular_exponentiation, binary_exponentiation_iterative
from backtracking.subsets import subsets
from backtracking.n_queens import solveNQueens
from backtracking.permute import permute
from backtracking.sudoku import Sudoku
from dp.coin_change import coinChange
from dp.max_subarray import maxSubArray
from dp.edit_distance import EditDistance

if __name__ == "__main__":
    # print(gcd(414, 662))
    # print(is_prime(2147483353))
    # print(expand(12345, 8))
    # print(expand(177130, 16))
    # print(modular_exponentiation(3, 644, 645))
    # print(binary_exponentiation_iterative(3,11))
    # print(generate_pseudo_random(4321, 378, 2310, 7829))
    # print(subsets([1,2,3]))
    # print(permute([1, 2, 3]))
    # print(solveNQueens(4))

    # board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
    #                                                                                                                                                                                                       ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # sudoku = Sudoku()
    # sudoku.solve(board)
    # print(board)

    # print(coinChange([1, 2, 5], 11) == 3)
    # print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
    print(EditDistance().solve("horse", "ros") == 3)
    print(EditDistance().solve("intention", "execution") == 5)