from pprint import pprint

def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that is not filled yet

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None #if no spaces are available

def is_valid(puzzle, guess, row, col):

    #determines whether the guess at row/col is a valid guess.
    #returns true if valid

    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row //3) *3
    col_start = (row //3) *3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False 
    #if the checks pass
    return True

def solve_sudoku(puzzle):
    #using baktracking to solve 
    #puzzle is a list of lists, where each inner list is a row in the puzzle
    #returns whether or not a solution exists and mutates the puzzle to be the solution (if the solution exists)

    row, col = find_next_empty(puzzle)

    #if there are no available spaces, done bc only allowed valid input

    if row is None:
        return True
    
    #if there is space, make guess 1-9
    for guess in range (1,10): 

        if is_valid(puzzle, guess, row, col):
            #place the guess on the row,col
            puzzle[row][col] = guess

            #use recursion 
            if solve_sudoku(puzzle):
                return True
            
        #backtrack and move on to next guess
        puzzle[row][col] = -1 #resets the guess

    #if none work, there is no solution
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
