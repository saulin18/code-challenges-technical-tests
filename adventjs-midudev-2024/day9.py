# 🚂 The magic train
# The elves are playing with a magical train 🚂 that carries gifts. This train moves on a board represented by an array 
# of strings.

# The train consists of an engine (@), followed by its carriages (o), and must collect magical fruits (*) which serve 
# as fuel. The movement of the train follows these rules:

# You will receive two parameters board and mov.
# board is an array of strings that represents the board:
# @ is the train's engine.
# o are the train's carriages.
# * is a magical fruit.
# · are empty spaces.
# mov is a string that indicates the next movement of the train from the train's head @:
# 'L': left
# 'R': right
# 'crash': If the train crashes into the edges of the board or itself.
# 'eat': If the train collects a magical fruit (*).
# 'none': If it moves without crashing or collecting any magical fruit.

# Example:
# 
# const board = ["·····", 
#               "*····", 
#               "@····", 
#               "o····", 
#               "o····"];
# 
# console.log(moveTrain(board, "U"));
# // ➞ 'eat'
# // Because the train moves up and finds a magical fruit
# 
# console.log(moveTrain(board, "D"));
# // ➞ 'crash'
# // The train moves down and the head crashes into itself
# 
# console.log(moveTrain(board, "L"));
# // ➞ 'crash'
# // The train moves to the left and crashes into the wall
# 
# console.log(moveTrain(board, "R"));
# // ➞ 'none'
# // The train moves to the right and there is empty space on the right

def move_train(board: list[str], mov: str) -> str:
    
    row_index = None
    column_index = None
    
    # First we need to find the position of the train's head @
    for i, row in enumerate(board):
        if "@" in row:
            row_index = i
            column_index = row.index("@")
            break
    
    possible_moves = {
        "L": (-1, 0),
        "R": (1, 0),
        # UP is bottom, so we move down
        "U": (1, 0),
        # DOWN is top
        "D": (-1, 0)
    }
    
    # Then we need to move the train's head @ according to the mov string
    for move in mov:
        new_row_index = row_index + possible_moves[move][0]
        new_column_index = column_index + possible_moves[move][1]
        
        if new_row_index < 0 or new_row_index >= len(board) or new_column_index < 0 or new_column_index >= len(board[0]):
            return "crash"
        
        if board[new_row_index][new_column_index] == "#":
            return "crash"
        
        if board[new_row_index][new_column_index] == "o":
            return "eat"
        
        row_index = new_row_index
        column_index = new_column_index
    
    return "none"

board = [
    "·····", 
    "*····", 
    "@····", 
    "o····", 
    "o····"
]

print(move_train(board, "U"))