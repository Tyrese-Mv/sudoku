from random import sample


def pattern(r, c, base, side):
    return (base * (r % base) + r // base + c) % side


def shuffle(s):
    return sample(s, len(s))

def generate_solution():
    
    base = 3
    side = base * base
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))
    
    board = [[nums[pattern(r, c, base, side)] for c in cols] for r in rows]
    
    return board
def hide_numbers(board):
    hidden_board = [row[:] for row in board]  

    cells_to_hide = sample(range(len(board) * len(board)), 60)

    for cell_index in cells_to_hide:
        row = cell_index // len(board)
        col = cell_index % len(board)
        hidden_board[row][col] = "."  

    return hidden_board

    