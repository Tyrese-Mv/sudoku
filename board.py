def empty_board():
    board = [[None for _ in range(9)] for _ in range(9)]
    
    print("+-----------------------------------------+")
    for i, row in enumerate(board):
        if i != 0 and i % 3 == 0:
            print("+-----------------------------------------+")
        for j, column in enumerate(row):
            
            if j == 0 or j % 3 == 0:
                print("|", end=" ")
            if column is None:
                print(" . ", end=" ")
            else:
                print(column, end=" ")
        print("|")
    print("+-----------------------------------------+")

if __name__ == "__main__":
    empty_board()
