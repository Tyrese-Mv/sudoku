from random import sample

# Pattern for a baseline valid solution
def pattern(r, c, base, side):
    return (base * (r % base) + r // base + c) % side

# Randomize rows, columns, and numbers (of valid base pattern)

def shuffle(s):
    return sample(s, len(s))

def generate_solution():
    # Define the base size (3 for a 9x9 Sudoku)
    base = 3
    side = base * base
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))
    # Produce the board using the randomized baseline pattern
    board = [[nums[pattern(r, c, base, side)] for c in cols] for r in rows]
    
    return board