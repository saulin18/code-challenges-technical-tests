# 🎄 Decorating the Christmas tree
# It's time to put up the Christmas tree at home! 🎄 But this year we want it to be special. We're going to create a function
# that receives the height of the tree (a positive integer between 1 and 100) and a special character to decorate it# 
# The function should return a string that represents the Christmas tree, constructed as follows:

# The tree is made up of triangles of special characters.
# The spaces on the sides of the tree are represented with underscores _.
# All trees have a trunk of two lines, represented by the # character.
# The tree should always have the same length on each side.
# You must ensure the tree has the correct shape using line breaks \n for each line.

# Examples:
# const tree = createXmasTree(5, "*");
# console.log(tree);
# /*
# ____*____
# ___***___
# __*****__
# _*******_
# *********
# ____#____
# ____#____
# */
# const tree2 = createXmasTree(3, "+");
# console.log(tree2);
# /*
# __+__
# _+++_
# +++++
# __#__
# __#__
# */
# const tree3 = createXmasTree(6, "@");
# console.log(tree3);
# /*
# _____@_____
# ____@@@____
# ___@@@@@___
# __@@@@@@@__
# _@@@@@@@@@_
# @@@@@@@@@@@
# _____#_____
# _____#_____
# */
# Make sure to use line breaks \n at the end of each line, except for the last one.
def create_xmas_tree(number_of_levels: int, symbol: str) -> str:
    
    # Is always this length in the examples
    length_of_row = (number_of_levels * 2) - 1
    
    rows = []
    # The rows of the bottom with the # in the center
    last_rows = "#".center(length_of_row, "_")
    
    number_of_symbols = 1
    for _ in range(number_of_levels):
        current_symbol_to_append = symbol * number_of_symbols
        row = current_symbol_to_append.center(length_of_row, "_")
        number_of_symbols += 2
        rows.append(row)
    
    rows.append(last_rows)
    rows.append(last_rows)
    
    return "\n".join(rows)


print(create_xmas_tree(5, "*"))