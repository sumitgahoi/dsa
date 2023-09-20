from maths.gcd import gcd
from maths.prime import is_prime, generate_pseudo_random
from maths.expand import expand, modular_exponentiation, binary_exponentiation_iterative
from backtracking.subsets import subsets
from backtracking.n_queens import solveNQueens
from backtracking.permute import permute

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
    print(solveNQueens(4))
