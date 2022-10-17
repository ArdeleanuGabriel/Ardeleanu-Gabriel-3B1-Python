#! /usr/bin/python3
import numpy as np


def matrix_diag_0(x: list[list[int]]):
    npx = np.array(x)
    np.fill_diagonal(npx, 0)
    return npx.tolist()

def main():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(f"New mat = { matrix_diag_0(mat)}")

if __name__ == "__main__":
    main()