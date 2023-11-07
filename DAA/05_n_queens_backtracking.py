""": Design n-Queens matrix having first Queen placed. Use backtracking to
place remaining Queens to generate the final n-queen’s matrix 
place remaining Queens to generate the final n-queen’s matrix."""

# def solveNQueens(n: int, first_queen_col: int):
#     col = set()
#     posDiag = set()
#     negDiag = set()

#     res = []
#     board = [["."] * n for _ in range(n)]

#     def backtrack(r):
#         if r == n:
#             res.append(["".join(row) for row in board])
#             return

#         for c in range(n):
#             if c in col or (r + c) in posDiag or (r - c) in negDiag:
#                 continue

#             col.add(c)
#             posDiag.add(r + c)
#             negDiag.add(r - c)
#             board[r][c] = "Q"

#             backtrack(r + 1)

#             col.remove(c)
#             posDiag.remove(r + c)
#             negDiag.remove(r - c)
#             board[r][c] = "."

#     col.add(first_queen_col)
#     posDiag.add(0 + first_queen_col)
#     negDiag.add(0 - first_queen_col)
#     board[0][first_queen_col] = "Q"

#     backtrack(1)  # Start with the second row
#     return res

# if __name__ == "__main__":
#     n = 8
#     first_queen_col = 1
#     board = solveNQueens(n, first_queen_col)[0]
#     for row in board:
#         print(" ".join(row))


# way 2nd

# Python3 program to solve N-Queens problem using backtracking

# Global N variable
N = 4

# Function to print the solution
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

# A utility function to check if a queen can be placed on board[row][col]
def isSafe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Recursive function to solve N-Queens problem
def solveNQUtil(board, col):
    # Base case: If all queens are placed, return true
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1):
                return True

            # If placing the queen in board[i][col] doesn't lead to a solution, then remove the queen
            board[i][col] = 0

    # If the queen can't be placed in any row in this column, return false
    return False

# Main function to solve N-Queens
def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

# Driver Code
solveNQ()
