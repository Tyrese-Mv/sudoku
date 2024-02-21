
import puzzle_generator
def empty_board():
    
    board = puzzle_generator.generate_solution()
    hidden = puzzle_generator.hide_numbers(board)
    
    print("+-----------------------+")
    for i, row in enumerate(hidden):
        if i != 0 and i % 3 == 0:
            print("+-----------------------+")
        for j, column in enumerate(row):
            
            if j == 0 or j % 3 == 0:
                print("|", end=" ")
            if column is None:
                print(" . ", end=" ")
            else:
                print(column, end=" ")
        print("|")
    print("+-----------------------+")

if __name__ == "__main__":
    empty_board()
